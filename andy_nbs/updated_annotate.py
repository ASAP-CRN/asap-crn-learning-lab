import numpy as np
import scanpy as sc
import decoupler as dc
import scvi
import pandas as pd

# Open the RNA merged and filtered
adata = sc.read_h5ad(snakemake.input.merged_rna_anndata)

doublet_clusters = []
for cluster in adata.obs["leiden_2"].drop_duplicates():
    # print(cluster, adata[adata.obs['leiden'] == cluster].obs['doublet_score'].mean(), adata[adata.obs['leiden'] == cluster].obs['doublet_score'].median())
    if adata[adata.obs["leiden_2"] == cluster].obs["doublet_score"].median() > 0.05:
        doublet_clusters.append(cluster)

adata = adata[~adata.obs["leiden_2"].isin(doublet_clusters)].copy()

# Create the DataFrame of canonical gene markers (This can be expanded)
marker_gene_df = pd.read_csv(snakemake.input.gene_markers)

doublet_clusters = []
for cluster in adata.obs["leiden"].drop_duplicates():
    # print(cluster, adata[adata.obs['leiden'] == cluster].obs['doublet_score'].mean(), adata[adata.obs['leiden'] == cluster].obs['doublet_score'].median())
    if adata[adata.obs["leiden"] == cluster].obs["doublet_score"].median() > 0.05:
        doublet_clusters.append(cluster)

adata = adata[~adata.obs["leiden"].isin(doublet_clusters)].copy()

# Run over-represenation analysis based on cell markers
# provided in the marker_gene_df DataFrame.
dc.run_ora(
    mat=adata,
    net=marker_gene_df,
    source="cell type",
    target="official gene symbol",
    min_n=1,
    verbose=True,
    use_raw=False,
)

# Create a mini AnnData object with the over-represenation
# analysis estimate (p-value of given cell marker)
acts = dc.get_acts(adata, obsm_key="ora_estimate")

# Convert the ORA AnnData object to numpy array to rank
# which cell type for each leiden cluster
acts_v = acts.X.ravel()
max_e = np.nanmax(acts_v[np.isfinite(acts_v)])
acts.X[~np.isfinite(acts.X)] = max_e
df = dc.rank_sources_groups(
    acts, groupby="leiden_2", reference="rest", method="t-test_overestim_var"
)

# ___________________


import decoupler as dc

adata, net = dc.ds.toy()
dc.mt.ora(adata, net, tmin=3)

# Run over-represenation analysis based on cell markers
# provided in the marker_gene_df DataFrame.

# import decoupler as dc
# adata, net = dc.ds.toy()
# (
#     mat: np.ndarray,
#     cnct: np.ndarray,
#     starts: np.ndarray,
#     offsets: np.ndarray,
#     n_up: int | float | None = None,
#     n_bm: int | float = 0,
#     n_bg: int | float | None = 20_000,
#     ha_corr: int | float = 0.5,
#     verbose: bool = False,
# ) -> tuple[np.ndarray, np.ndarray]:

# Create a mini AnnData object with the over-represenation
# analysis estimate (p-value of given cell marker)
acts = dc.get_obsm(
    adata,
    net=marker_gene_df,
    source="cell type",
    target="official gene symbol",
    min_n=1,
    verbose=True,
    use_raw=False,
    obsm_key="ora_estimate",
)

# adata, net = dc.ds.toy()
# dc.mt.ulm(adata, net, tmin=3)
# scores = dc.pp.get_obsm(adata, "score_ulm")
# dc.tl.rankby_group(adata, groupby="group")

# this "tools" == tl method should add it back to adata
dc.tl.rankby_group(
    adata, groupby="leiden_2", reference="rest", method="t-test_overestim_var"
)


# ___________________

# Apply the best ranked cell type to a cluster-celltype dictionary
annotation_dict = df.groupby("group").head(1).set_index("group")["names"].to_dict()

# Apply the dictionary to the AnnData object
adata.obs["cell_type"] = [annotation_dict[clust] for clust in adata.obs["leiden_2"]]

# Save the cell barcode, cluster, cell-type, and batch values to a .csv
adata.obs[
    ["atlas_identifier", "leiden_2", "cell_type", snakemake.params.seq_batch_key]
].to_csv(snakemake.output.cell_annotate, index=False)


# Save the annotated AnnData object
adata.write_h5ad(filename=snakemake.output.merged_rna_anndata, compression="gzip")
