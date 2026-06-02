# CRN Cloud Releases

Browse CRN Cloud release records generated from release JSON. Use the filter to search by release, CDE version, dataset name, dataset version, or DOI.

<input id="releaseSearch" class="release-search" type="text" placeholder="Filter releases, datasets, versions, or DOIs...">

<p id="releaseCount" class="release-count"></p>

<style>
.release-search {
  width: 100%;
  padding: 0.75rem;
  margin: 1rem 0 0.5rem 0;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.45rem;
  font-size: 1rem;
}
.release-count {
  margin: 0 0 1rem 0;
  color: var(--md-default-fg-color--light);
}
.release-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1rem;
}
.release-card {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.7rem;
  padding: 1rem;
  cursor: pointer;
  background: var(--md-default-bg-color);
}
.release-card:hover {
  border-color: var(--md-accent-fg-color);
  box-shadow: 0 0.2rem 0.6rem rgba(0,0,0,0.08);
}
.release-card h3 {
  margin-top: 0;
  margin-bottom: 0.35rem;
}
.release-card p {
  margin: 0.35rem 0;
}
.release-modal {
  display: none;
  position: fixed;
  z-index: 9999;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.45);
  align-items: flex-start;
  justify-content: center;
  overflow: auto;
  padding: 3rem 1rem;
}
.release-modal-content {
  width: min(950px, 95vw);
  background: var(--md-default-bg-color);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 0.4rem 1.5rem rgba(0,0,0,0.25);
}
.release-modal-close {
  float: right;
  font-size: 1.6rem;
  font-weight: bold;
  cursor: pointer;
}
.release-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}
.release-table th, .release-table td {
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
  padding: 0.55rem;
  text-align: left;
  vertical-align: top;
}
</style>

<div class="release-grid" id="releaseGrid">
<div class="release-card" data-modal="release-modal-v4-1-1-0" data-search="v4.1.1 v4.1.1 v4.4 10.5281/zenodo.20185963 hafler-pmdbs-sn-rnaseq-pfc v1.1 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.16744323 scherzer-pmdbs-sn-rnaseq-mtg v1.2 10.5281/zenodo.16751625 hardy-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.1 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.1 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.1 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.2 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v3.1.1 10.5281/zenodo.19876217 cohort-pmdbs-bulk-rnaseq v1.2.1 10.5281/zenodo.16975686 jakobsson-pmdbs-sn-rnaseq v2.1 10.5281/zenodo.15162834 biederer-mouse-sc-rnaseq v1.0 10.5281/zenodo.15485103 cragg-mouse-sn-rnaseq-striatum v1.0 10.5281/zenodo.15400039 edwards-pmdbs-spatial-geomx-th v1.0 10.5281/zenodo.15480990 cragg-mouse-spatial-visium-striatum v1.0 10.5281/zenodo.15428115 jakobsson-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16929448 alessi-invitro-ms-p-hek293-gtip v1.1 10.5281/zenodo.17355407 schlossmacher-mouse-sn-rnaseq-osn-aav-transd v1.0 10.5281/zenodo.17358327 scherzer-pmdbs-spatial-visium-mtg v1.1 10.5281/zenodo.17242087 scherzer-pmdbs-genetics v1.1 10.5281/zenodo.17242295 alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s v1.0 10.5281/zenodo.17212215 jakobsson-invitro-bulk-rnaseq-dopaminergic v1.0 10.5281/zenodo.17149266 jakobsson-invitro-bulk-rnaseq-microglia v1.0 10.5281/zenodo.17149290 sulzer-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.17612853 cohort-mouse-sc-rnaseq v1.0.0 10.5281/zenodo.17860975 schapira-fecal-metagenome-human-baseline v1.0 10.5281/zenodo.18353680 lee-mouse-liver-bulk-rnaseq-g2019s v1.0 10.5281/zenodo.18273810 lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet v1.0 10.5281/zenodo.18273802 lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet v1.0 10.5281/zenodo.18273808 liddle-human-colon-spatial-cosmx-rna-1000p v1.0 10.5281/zenodo.17917788 liddle-human-colon-spatial-cosmx-protein-64p v1.0 10.5281/zenodo.17917771 alessi-mefs-ms-p-vps35-d620n-wt v1.0 10.5281/zenodo.18476408 alessi-mefs-ms-p-vps35-d620n-dmso-mli2 v1.0 10.5281/zenodo.18476410 sulzer-fecal-metagenome-fp-spf v1.0 10.5281/zenodo.18989559 lee-mouse-ms-p-lung-g2019s-hf-diet v1.0 10.5281/zenodo.18273812 lee-mouse-ms-mb-plasma-g2019s-hf-diet v1.0 10.5281/zenodo.18273818 lee-mouse-ms-mb-liver-g2019s-hf-diet v1.0 10.5281/zenodo.18273822 lee-mouse-ms-mb-striatum-g2019s-hf-diet v1.0 10.5281/zenodo.18273824 lee-mouse-ms-mb-lung-g2019s-hf-diet v1.0 10.5281/zenodo.18273832 lee-mouse-ms-mb-kidney-g2019s-hf-diet v1.0 10.5281/zenodo.18273834 lee-mouse-ms-l-plasma-g2019s-hf-diet v1.0 10.5281/zenodo.18273840 lee-mouse-ms-l-liver-g2019s-hf-diet v1.0 10.5281/zenodo.18273844 lee-mouse-ms-l-striatum-g2019s-hf-diet v1.0 10.5281/zenodo.18273848 lee-mouse-ms-l-lung-g2019s-hf-diet v1.0 10.5281/zenodo.18273852 lee-mouse-ms-l-kidney-g2019s-hf-diet v1.0 10.5281/zenodo.18273858 lee-mouse-ms-mb-plasma-g2019s-nuc-quant v1.0 10.5281/zenodo.18273863 lee-mouse-ms-mb-striatum-g2019s-nuc-quant v1.0 10.5281/zenodo.18273868 lee-mouse-ms-mb-midbrain-g2019s-nuc-quant v1.0 10.5281/zenodo.18273870 alessi-mouse-ms-p-lung-vps35-d620n-wt v1.0 10.5281/zenodo.18476393 alessi-mouse-ms-p-brain-vps35-d620n-wt v1.0 10.5281/zenodo.18476398 alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2 v1.0 10.5281/zenodo.18476402 alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2 v1.0 10.5281/zenodo.18476404 voet-pmdbs-sn-multimodal v1.0 10.5281/zenodo.18988753 voet-pmdbs-sn-atacseq-scalebio-hydrop v1.0 10.5281/zenodo.18988743 voet-pmdbs-sn-atacseq-scalebio-10x v1.0 10.5281/zenodo.18988717 voet-pmdbs-sn-atacseq-hydrop v1.0 10.5281/zenodo.18988735 voet-pmdbs-sn-atacseq-10x v1.0 10.5281/zenodo.18988729 voet-pmdbs-sn-rnaseq-parsebio v1.0 10.5281/zenodo.18988761 voet-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.18988768 scherzer-pmdbs-sn-rnaseq-midbrain-hybsel v1.0 10.5281/zenodo.19124469 scherzer-pmdbs-lr-wgs v1.0 10.5281/zenodo.19124632">
  <h3>CRN Cloud Release v4.1.1</h3>
  <p><code>v4.1.1</code></p>
  <p><strong>Release version:</strong> v4.1.1</p>
  <p><strong>CDE version:</strong> v4.4</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.20185963" target="_blank" rel="noopener">10.5281/zenodo.20185963</a></p>
  <p><em>Click card to view 61 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v4-1-0-1" data-search="v4.1.0 v4.1.0 v4.3 10.5281/zenodo.19740716 hafler-pmdbs-sn-rnaseq-pfc v1.1 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.16744323 scherzer-pmdbs-sn-rnaseq-mtg v1.2 10.5281/zenodo.16751625 hardy-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.1 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.1 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.1 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.2 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v3.1.1 10.5281/zenodo.19876217 cohort-pmdbs-bulk-rnaseq v1.2.1 10.5281/zenodo.16975686 jakobsson-pmdbs-sn-rnaseq v2.1 10.5281/zenodo.15162834 biederer-mouse-sc-rnaseq v1.0 10.5281/zenodo.15485103 cragg-mouse-sn-rnaseq-striatum v1.0 10.5281/zenodo.15400039 edwards-pmdbs-spatial-geomx-th v1.0 10.5281/zenodo.15480990 cragg-mouse-spatial-visium-striatum v1.0 10.5281/zenodo.15428115 jakobsson-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16929448 alessi-invitro-ms-p-hek293-gtip v1.1 10.5281/zenodo.17355407 schlossmacher-mouse-sn-rnaseq-osn-aav-transd v1.0 10.5281/zenodo.17358327 scherzer-pmdbs-spatial-visium-mtg v1.1 10.5281/zenodo.17242087 scherzer-pmdbs-genetics v1.1 10.5281/zenodo.17242295 alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s v1.0 10.5281/zenodo.17212215 jakobsson-invitro-bulk-rnaseq-dopaminergic v1.0 10.5281/zenodo.17149266 jakobsson-invitro-bulk-rnaseq-microglia v1.0 10.5281/zenodo.17149290 sulzer-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.17612853 cohort-mouse-sc-rnaseq v1.0.0 10.5281/zenodo.17860975 schapira-fecal-metagenome-human-baseline v1.0 10.5281/zenodo.18353680 lee-mouse-liver-bulk-rnaseq-g2019s v1.0 10.5281/zenodo.18273810 lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet v1.0 10.5281/zenodo.18273802 lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet v1.0 10.5281/zenodo.18273808 liddle-human-colon-spatial-cosmx-rna-1000p v1.0 10.5281/zenodo.17917788 liddle-human-colon-spatial-cosmx-protein-64p v1.0 10.5281/zenodo.17917771 alessi-mefs-ms-p-vps35-d620n-wt v1.0 10.5281/zenodo.18476408 alessi-mefs-ms-p-vps35-d620n-dmso-mli2 v1.0 10.5281/zenodo.18476410 sulzer-fecal-metagenome-fp-spf v1.0 10.5281/zenodo.18989559 lee-mouse-ms-p-lung-g2019s-hf-diet v1.0 10.5281/zenodo.18273812 lee-mouse-ms-mb-plasma-g2019s-hf-diet v1.0 10.5281/zenodo.18273818 lee-mouse-ms-mb-liver-g2019s-hf-diet v1.0 10.5281/zenodo.18273822 lee-mouse-ms-mb-striatum-g2019s-hf-diet v1.0 10.5281/zenodo.18273824 lee-mouse-ms-mb-lung-g2019s-hf-diet v1.0 10.5281/zenodo.18273832 lee-mouse-ms-mb-kidney-g2019s-hf-diet v1.0 10.5281/zenodo.18273834 lee-mouse-ms-l-plasma-g2019s-hf-diet v1.0 10.5281/zenodo.18273840 lee-mouse-ms-l-liver-g2019s-hf-diet v1.0 10.5281/zenodo.18273844 lee-mouse-ms-l-striatum-g2019s-hf-diet v1.0 10.5281/zenodo.18273848 lee-mouse-ms-l-lung-g2019s-hf-diet v1.0 10.5281/zenodo.18273852 lee-mouse-ms-l-kidney-g2019s-hf-diet v1.0 10.5281/zenodo.18273858 lee-mouse-ms-mb-plasma-g2019s-nuc-quant v1.0 10.5281/zenodo.18273863 lee-mouse-ms-mb-striatum-g2019s-nuc-quant v1.0 10.5281/zenodo.18273868 lee-mouse-ms-mb-midbrain-g2019s-nuc-quant v1.0 10.5281/zenodo.18273870 alessi-mouse-ms-p-lung-vps35-d620n-wt v1.0 10.5281/zenodo.18476393 alessi-mouse-ms-p-brain-vps35-d620n-wt v1.0 10.5281/zenodo.18476398 alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2 v1.0 10.5281/zenodo.18476402 alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2 v1.0 10.5281/zenodo.18476404">
  <h3>CRN Cloud Release v4.1.0</h3>
  <p><code>v4.1.0</code></p>
  <p><strong>Release version:</strong> v4.1.0</p>
  <p><strong>CDE version:</strong> v4.3</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.19740716" target="_blank" rel="noopener">10.5281/zenodo.19740716</a></p>
  <p><em>Click card to view 52 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v4-0-2-2" data-search="v4.0.2 v4.0.2 v4.2 10.5281/zenodo.19289362 hafler-pmdbs-sn-rnaseq-pfc v1.1 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.16744323 scherzer-pmdbs-sn-rnaseq-mtg v1.2 10.5281/zenodo.16751625 hardy-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.1 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.1 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.1 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.2 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v3.1.1 10.5281/zenodo.19876217 cohort-pmdbs-bulk-rnaseq v1.2.1 10.5281/zenodo.16975686 jakobsson-pmdbs-sn-rnaseq v2.1 10.5281/zenodo.15162834 biederer-mouse-sc-rnaseq v1.0 10.5281/zenodo.15485103 cragg-mouse-sn-rnaseq-striatum v1.0 10.5281/zenodo.15400039 edwards-pmdbs-spatial-geomx-th v1.0 10.5281/zenodo.15480990 cragg-mouse-spatial-visium-striatum v1.0 10.5281/zenodo.15428115 jakobsson-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16929448 alessi-invitro-ms-p-hek293-gtip v1.1 10.5281/zenodo.17355407 schlossmacher-mouse-sn-rnaseq-osn-aav-transd v1.0 10.5281/zenodo.17358327 scherzer-pmdbs-spatial-visium-mtg v1.1 10.5281/zenodo.17242087 scherzer-pmdbs-genetics v1.1 10.5281/zenodo.17242295 alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s v1.0 10.5281/zenodo.17212215 jakobsson-invitro-bulk-rnaseq-dopaminergic v1.0 10.5281/zenodo.17149266 jakobsson-invitro-bulk-rnaseq-microglia v1.0 10.5281/zenodo.17149290 sulzer-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.17612853 cohort-mouse-sc-rnaseq v1.0.0 10.5281/zenodo.17860975 schapira-fecal-metagenome-human-baseline v1.0 10.5281/zenodo.18353680 lee-mouse-liver-bulk-rnaseq-g2019s v1.0 10.5281/zenodo.18273810 lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet v1.0 10.5281/zenodo.18273802 lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet v1.0 10.5281/zenodo.18273808 liddle-human-colon-spatial-cosmx-rna-1000p v1.0 10.5281/zenodo.17917788 liddle-human-colon-spatial-cosmx-protein-64p v1.0 10.5281/zenodo.17917771 alessi-mefs-ms-p-vps35-d620n-wt v1.0 10.5281/zenodo.18476408 alessi-mefs-ms-p-vps35-d620n-dmso-mli2 v1.0 10.5281/zenodo.18476410 sulzer-fecal-metagenome-fp-spf v1.0 10.5281/zenodo.18989559 alessi-invitro-ms-p-hek293-gtip v1.1 10.5281/zenodo.17355407">
  <h3>CRN Cloud Release v4.0.2</h3>
  <p><code>v4.0.2</code></p>
  <p><strong>Release version:</strong> v4.0.2</p>
  <p><strong>CDE version:</strong> v4.2</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.19289362" target="_blank" rel="noopener">10.5281/zenodo.19289362</a></p>
  <p><em>Click card to view 35 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v4-0-2-3" data-search="v4.0.2 v4.0.2   ">
  <h3>CRN Cloud Release v4.0.2</h3>
  <p><code>v4.0.2</code></p>
  <p><strong>Release version:</strong> v4.0.2</p>
  <p><strong>CDE version:</strong> TBD</p>
  <p><strong>Release DOI:</strong> TBD</p>
  <p><em>Click card to view 0 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v4-0-1-4" data-search="v4.0.1 v4.0.1 v4.1 10.5281/zenodo.18780122 hafler-pmdbs-sn-rnaseq-pfc v1.1 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.16744323 scherzer-pmdbs-sn-rnaseq-mtg v1.2 10.5281/zenodo.16751625 hardy-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.1 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.1 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.1 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.2 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v3.1.1 10.5281/zenodo.19876217 cohort-pmdbs-bulk-rnaseq v1.2.1 10.5281/zenodo.16975686 jakobsson-pmdbs-sn-rnaseq v2.1 10.5281/zenodo.15162834 biederer-mouse-sc-rnaseq v1.0 10.5281/zenodo.15485103 cragg-mouse-sn-rnaseq-striatum v1.0 10.5281/zenodo.15400039 edwards-pmdbs-spatial-geomx-th v1.0 10.5281/zenodo.15480990 cragg-mouse-spatial-visium-striatum v1.0 10.5281/zenodo.15428115 jakobsson-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16929448 alessi-invitro-ms-p-hek293-gtip v1.1 10.5281/zenodo.17355407 schlossmacher-mouse-sn-rnaseq-osn-aav-transd v1.0 10.5281/zenodo.17358327 scherzer-pmdbs-spatial-visium-mtg v1.1 10.5281/zenodo.17242087 scherzer-pmdbs-genetics v1.1 10.5281/zenodo.17242295 alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s v1.0 10.5281/zenodo.17212215 jakobsson-invitro-bulk-rnaseq-dopaminergic v1.0 10.5281/zenodo.17149266 jakobsson-invitro-bulk-rnaseq-microglia v1.0 10.5281/zenodo.17149290 sulzer-pmdbs-sn-rnaseq v1.1 10.5281/zenodo.17612853 cohort-mouse-sc-rnaseq v1.0.0 10.5281/zenodo.17860975 schapira-fecal-metagenome-human-baseline v1.0 10.5281/zenodo.18353680 lee-mouse-liver-bulk-rnaseq-g2019s v1.0 10.5281/zenodo.18273810 lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet v1.0 10.5281/zenodo.18273802 lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet v1.0 10.5281/zenodo.18273808 liddle-human-colon-spatial-cosmx-rna-1000p v1.0 10.5281/zenodo.17917788 liddle-human-colon-spatial-cosmx-protein-64p v1.0 10.5281/zenodo.17917771">
  <h3>CRN Cloud Release v4.0.1</h3>
  <p><code>v4.0.1</code></p>
  <p><strong>Release version:</strong> v4.0.1</p>
  <p><strong>CDE version:</strong> v4.1</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18780122" target="_blank" rel="noopener">10.5281/zenodo.18780122</a></p>
  <p><em>Click card to view 31 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v4-0-0-5" data-search="v4.0.0 v4.0.0 v3.3 10.5281/zenodo.17834620 hafler-pmdbs-sn-rnaseq-pfc v1.0 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16744323 scherzer-pmdbs-sn-rnaseq-mtg v1.1 10.5281/zenodo.16751625 hardy-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.0 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.1 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v3.1.0 10.5281/zenodo.17860778 cohort-pmdbs-bulk-rnaseq v1.2.0 10.5281/zenodo.17860841 jakobsson-pmdbs-sn-rnaseq v2.0 10.5281/zenodo.15162834 biederer-mouse-sc-rnaseq v1.0 10.5281/zenodo.15485103 cragg-mouse-sn-rnaseq-striatum v1.0 10.5281/zenodo.15400039 edwards-pmdbs-spatial-geomx-th v1.0 10.5281/zenodo.15480990 cragg-mouse-spatial-visium-striatum v1.0 10.5281/zenodo.15428115 jakobsson-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16929448 alessi-invitro-ms-p-hek293-gtip v1.0 10.5281/zenodo.16751625 schlossmacher-mouse-sn-rnaseq-osn-aav-transd v1.0 10.5281/zenodo.17358327 scherzer-pmdbs-spatial-visium-mtg v1.0 10.5281/zenodo.17242087 scherzer-pmdbs-genetics v1.0 10.5281/zenodo.17242295 alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s v1.0 10.5281/zenodo.17212215 jakobsson-invitro-bulk-rnaseq-dopaminergic v1.0 10.5281/zenodo.17149266 jakobsson-invitro-bulk-rnaseq-microglia v1.0 10.5281/zenodo.17149290 sulzer-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.17612853 cohort-mouse-sc-rnaseq v1.0.0 10.5281/zenodo.17860975">
  <h3>CRN Cloud Release v4.0.0</h3>
  <p><code>v4.0.0</code></p>
  <p><strong>Release version:</strong> v4.0.0</p>
  <p><strong>CDE version:</strong> v3.3</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17834620" target="_blank" rel="noopener">10.5281/zenodo.17834620</a></p>
  <p><em>Click card to view 25 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v4-0-0-6" data-search="v4.0.0 v4.0.0   ">
  <h3>CRN Cloud Release v4.0.0</h3>
  <p><code>v4.0.0</code></p>
  <p><strong>Release version:</strong> v4.0.0</p>
  <p><strong>CDE version:</strong> TBD</p>
  <p><strong>Release DOI:</strong> TBD</p>
  <p><em>Click card to view 0 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v3-0-2-7" data-search="v3.0.2 v3.0.2 v3.2 10.5281/zenodo.17727566 hafler-pmdbs-sn-rnaseq-pfc v1.0 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16744323 scherzer-pmdbs-sn-rnaseq-mtg v1.1 10.5281/zenodo.16751625 hardy-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.0 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.1 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v3.0.0 10.5281/zenodo.16979638 cohort-pmdbs-bulk-rnaseq v1.1.0 10.5281/zenodo.16975686 jakobsson-pmdbs-sn-rnaseq v2.0 10.5281/zenodo.15162834 biederer-mouse-sc-rnaseq v1.0 10.5281/zenodo.15485103 cragg-mouse-sn-rnaseq-striatum v1.0 10.5281/zenodo.15400039 edwards-pmdbs-spatial-geomx-th v1.0 10.5281/zenodo.15480990 cragg-mouse-spatial-visium-striatum v1.0 10.5281/zenodo.15428115 jakobsson-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16929448 alessi-invitro-ms-p-hek293-gtip v1.0 10.5281/zenodo.16751625 schlossmacher-mouse-sn-rnaseq-osn-aav-transd v1.0 10.5281/zenodo.17358327 scherzer-pmdbs-spatial-visium-mtg v1.0 10.5281/zenodo.17242087 scherzer-pmdbs-genetics v1.0 10.5281/zenodo.17242295 alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s v1.0 10.5281/zenodo.17212215 jakobsson-invitro-bulk-rnaseq-dopaminergic v1.0 10.5281/zenodo.17149266 jakobsson-invitro-bulk-rnaseq-microglia v1.0 10.5281/zenodo.17149290">
  <h3>CRN Cloud Release v3.0.2</h3>
  <p><code>v3.0.2</code></p>
  <p><strong>Release version:</strong> v3.0.2</p>
  <p><strong>CDE version:</strong> v3.2</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17727566" target="_blank" rel="noopener">10.5281/zenodo.17727566</a></p>
  <p><em>Click card to view 23 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v3-0-2-8" data-search="v3.0.2 v3.0.2   ">
  <h3>CRN Cloud Release v3.0.2</h3>
  <p><code>v3.0.2</code></p>
  <p><strong>Release version:</strong> v3.0.2</p>
  <p><strong>CDE version:</strong> TBD</p>
  <p><strong>Release DOI:</strong> TBD</p>
  <p><em>Click card to view 0 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v3-0-1-9" data-search="v3.0.1 v3.0.1 v3.2 10.5281/zenodo.17497025 hafler-pmdbs-sn-rnaseq-pfc v1.0 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16744323 scherzer-pmdbs-sn-rnaseq-mtg v1.1 10.5281/zenodo.16751625 hardy-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.0 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.1 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v3.0.0 10.5281/zenodo.16979638 cohort-pmdbs-bulk-rnaseq v1.1.0 10.5281/zenodo.16975686 jakobsson-pmdbs-sn-rnaseq v2.0 10.5281/zenodo.15162834 biederer-mouse-sc-rnaseq v1.0 10.5281/zenodo.15485103 cragg-mouse-sn-rnaseq-striatum v1.0 10.5281/zenodo.15400039 edwards-pmdbs-spatial-geomx-th v1.0 10.5281/zenodo.15480990 cragg-mouse-spatial-visium-striatum v1.0 10.5281/zenodo.15428115 jakobsson-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16929448 alessi-invitro-ms-p-hek293-gtip v1.0 10.5281/zenodo.16751625 schlossmacher-mouse-sn-rnaseq-osn-aav-transd v1.0 10.5281/zenodo.17358327 scherzer-pmdbs-spatial-visium-mtg v1.0 10.5281/zenodo.17242087 scherzer-pmdbs-genetics v1.0 10.5281/zenodo.17242295 alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s v1.0 10.5281/zenodo.17212215">
  <h3>CRN Cloud Release v3.0.1</h3>
  <p><code>v3.0.1</code></p>
  <p><strong>Release version:</strong> v3.0.1</p>
  <p><strong>CDE version:</strong> v3.2</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17497025" target="_blank" rel="noopener">10.5281/zenodo.17497025</a></p>
  <p><em>Click card to view 21 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v3-0-1-10" data-search="v3.0.1 v3.0.1   ">
  <h3>CRN Cloud Release v3.0.1</h3>
  <p><code>v3.0.1</code></p>
  <p><strong>Release version:</strong> v3.0.1</p>
  <p><strong>CDE version:</strong> TBD</p>
  <p><strong>Release DOI:</strong> TBD</p>
  <p><em>Click card to view 0 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v3-0-0-11" data-search="v3.0.0 v3.0.0 v3.2 10.5281/zenodo.16975257 hafler-pmdbs-sn-rnaseq-pfc v1.0 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16744323 scherzer-pmdbs-sn-rnaseq-mtg v1.0 10.5281/zenodo.16885831 hardy-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.0 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.0 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v3.0.0 10.5281/zenodo.16979638 cohort-pmdbs-bulk-rnaseq v1.1.0 10.5281/zenodo.16975686 jakobsson-pmdbs-sn-rnaseq v2.0 10.5281/zenodo.15162834 biederer-mouse-sc-rnaseq v1.0 10.5281/zenodo.15485103 cragg-mouse-sn-rnaseq-striatum v1.0 10.5281/zenodo.15400039 edwards-pmdbs-spatial-geomx-th v1.0 10.5281/zenodo.15480990 cragg-mouse-spatial-visium-striatum v1.0 10.5281/zenodo.15428115 jakobsson-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16929448">
  <h3>CRN Cloud Release v3.0.0</h3>
  <p><code>v3.0.0</code></p>
  <p><strong>Release version:</strong> v3.0.0</p>
  <p><strong>CDE version:</strong> v3.2</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16975257" target="_blank" rel="noopener">10.5281/zenodo.16975257</a></p>
  <p><em>Click card to view 16 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v3-0-0-12" data-search="v3.0.0 v3.0.0   ">
  <h3>CRN Cloud Release v3.0.0</h3>
  <p><code>v3.0.0</code></p>
  <p><strong>Release version:</strong> v3.0.0</p>
  <p><strong>CDE version:</strong> TBD</p>
  <p><strong>Release DOI:</strong> TBD</p>
  <p><em>Click card to view 0 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v2-0-3-13" data-search="v2.0.3 v2.0.3 v3.0 10.5281/zenodo.15831618 hafler-pmdbs-sn-rnaseq-pfc v1.0 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16744323 jakobsson-pmdbs-sn-rnaseq v2.0 10.5281/zenodo.15162834 scherzer-pmdbs-sn-rnaseq-mtg v1.0 10.5281/zenodo.16885831 hardy-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.0 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.0 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v2.0.0 10.5281/zenodo.14373047 cohort-pmdbs-bulk-rnaseq v1.0.0 10.5281/zenodo.14373343 biederer-mouse-sc-rnaseq v1.0 10.5281/zenodo.15485103 cragg-mouse-sn-rnaseq-striatum v1.0 10.5281/zenodo.15400039 edwards-pmdbs-spatial-geomx-th v1.0 10.5281/zenodo.15480990 cragg-mouse-spatial-visium-striatum v1.0 10.5281/zenodo.15428115">
  <h3>CRN Cloud Release v2.0.3</h3>
  <p><code>v2.0.3</code></p>
  <p><strong>Release version:</strong> v2.0.3</p>
  <p><strong>CDE version:</strong> v3.0</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15831618" target="_blank" rel="noopener">10.5281/zenodo.15831618</a></p>
  <p><em>Click card to view 15 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v2-0-3-14" data-search="v2.0.3 v2.0.3   ">
  <h3>CRN Cloud Release v2.0.3</h3>
  <p><code>v2.0.3</code></p>
  <p><strong>Release version:</strong> v2.0.3</p>
  <p><strong>CDE version:</strong> TBD</p>
  <p><strong>Release DOI:</strong> TBD</p>
  <p><em>Click card to view 0 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v2-0-2-15" data-search="v2.0.2 v2.0.2 v3.0 10.5281/zenodo.15831618 hafler-pmdbs-sn-rnaseq-pfc v1.0 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16744323 jakobsson-pmdbs-sn-rnaseq v2.0 10.5281/zenodo.15162834 scherzer-pmdbs-sn-rnaseq-mtg v1.0 10.5281/zenodo.16885831 hardy-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.0 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.0 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v2.0.0 10.5281/zenodo.14373047 cohort-pmdbs-bulk-rnaseq v1.0.0 10.5281/zenodo.14373343 biederer-mouse-sc-rnaseq v1.0 10.5281/zenodo.15485103 cragg-mouse-sn-rnaseq-striatum v1.0 10.5281/zenodo.15400039 edwards-pmdbs-spatial-geomx-th v1.0 10.5281/zenodo.15480990">
  <h3>CRN Cloud Release v2.0.2</h3>
  <p><code>v2.0.2</code></p>
  <p><strong>Release version:</strong> v2.0.2</p>
  <p><strong>CDE version:</strong> v3.0</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15831618" target="_blank" rel="noopener">10.5281/zenodo.15831618</a></p>
  <p><em>Click card to view 14 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v2-0-2-16" data-search="v2.0.2 v2.0.2   ">
  <h3>CRN Cloud Release v2.0.2</h3>
  <p><code>v2.0.2</code></p>
  <p><strong>Release version:</strong> v2.0.2</p>
  <p><strong>CDE version:</strong> TBD</p>
  <p><strong>Release DOI:</strong> TBD</p>
  <p><em>Click card to view 0 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v2-0-1-17" data-search="v2.0.1 v2.0.1 v3.0 10.5281/zenodo.15831558 hafler-pmdbs-sn-rnaseq-pfc v1.0 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16744323 jakobsson-pmdbs-sn-rnaseq v2.0 10.5281/zenodo.15162834 scherzer-pmdbs-sn-rnaseq-mtg v1.0 10.5281/zenodo.16885831 hardy-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.0 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.0 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v2.0.0 10.5281/zenodo.14373047 cohort-pmdbs-bulk-rnaseq v1.0.0 10.5281/zenodo.14373343">
  <h3>CRN Cloud Release v2.0.1</h3>
  <p><code>v2.0.1</code></p>
  <p><strong>Release version:</strong> v2.0.1</p>
  <p><strong>CDE version:</strong> v3.0</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15831558" target="_blank" rel="noopener">10.5281/zenodo.15831558</a></p>
  <p><em>Click card to view 11 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v2-0-1-18" data-search="v2.0.1 v2.0.1   ">
  <h3>CRN Cloud Release v2.0.1</h3>
  <p><code>v2.0.1</code></p>
  <p><strong>Release version:</strong> v2.0.1</p>
  <p><strong>CDE version:</strong> TBD</p>
  <p><strong>Release DOI:</strong> TBD</p>
  <p><em>Click card to view 0 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v2-0-0-19" data-search="v2.0.0 v2.0.0 v3.0 10.5281/zenodo.14270014 hafler-pmdbs-sn-rnaseq-pfc v1.0 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16744323 jakobsson-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.15162834 scherzer-pmdbs-sn-rnaseq-mtg v1.0 10.5281/zenodo.16885831 hardy-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16749080 hardy-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749098 lee-pmdbs-bulk-rnaseq-mfg v1.0 10.5281/zenodo.16748937 wood-pmdbs-bulk-rnaseq v1.0 10.5281/zenodo.16749007 scherzer-pmdbs-sn-rnaseq-mtg-hybsel v1.0 10.5281/zenodo.16885839 cohort-pmdbs-sc-rnaseq v2.0.0 10.5281/zenodo.14373048 cohort-pmdbs-bulk-rnaseq v1.0.0 10.5281/zenodo.14373344">
  <h3>CRN Cloud Release v2.0.0</h3>
  <p><code>v2.0.0</code></p>
  <p><strong>Release version:</strong> v2.0.0</p>
  <p><strong>CDE version:</strong> v3.0</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.14270014" target="_blank" rel="noopener">10.5281/zenodo.14270014</a></p>
  <p><em>Click card to view 11 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v2-0-0-20" data-search="v2.0.0 v2.0.0   ">
  <h3>CRN Cloud Release v2.0.0</h3>
  <p><code>v2.0.0</code></p>
  <p><strong>Release version:</strong> v2.0.0</p>
  <p><strong>CDE version:</strong> TBD</p>
  <p><strong>Release DOI:</strong> TBD</p>
  <p><em>Click card to view 0 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v1-0-0-21" data-search="v1.0.0 v1.0.0 v2.1 10.5281/zenodo.11585274 hafler-pmdbs-sn-rnaseq-pfc v1.0 10.5281/zenodo.15490150 lee-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.16744323 jakobsson-pmdbs-sn-rnaseq v1.0 10.5281/zenodo.15162834 scherzer-pmdbs-sn-rnaseq-mtg v1.0 10.5281/zenodo.16885831 cohort-pmdbs-sc-rnaseq v1.0.0 10.5281/zenodo.14373047">
  <h3>CRN Cloud Release v1.0.0</h3>
  <p><code>v1.0.0</code></p>
  <p><strong>Release version:</strong> v1.0.0</p>
  <p><strong>CDE version:</strong> v2.1</p>
  <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.11585274" target="_blank" rel="noopener">10.5281/zenodo.11585274</a></p>
  <p><em>Click card to view 5 dataset(s)</em></p>
</div>
<div class="release-card" data-modal="release-modal-v1-0-0-22" data-search="v1.0.0 v1.0.0   ">
  <h3>CRN Cloud Release v1.0.0</h3>
  <p><code>v1.0.0</code></p>
  <p><strong>Release version:</strong> v1.0.0</p>
  <p><strong>CDE version:</strong> TBD</p>
  <p><strong>Release DOI:</strong> TBD</p>
  <p><em>Click card to view 0 dataset(s)</em></p>
</div>
</div>

<div id="release-modal-v4-1-1-0" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v4.1.1</h2>
    <p><strong>Release ID:</strong> <code>v4.1.1</code></p>
    <p><strong>CDE version:</strong> v4.4</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.20185963" target="_blank" rel="noopener">10.5281/zenodo.20185963</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.2</td>
          <td><a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.2</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v3.1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.19876217" target="_blank" rel="noopener">10.5281/zenodo.19876217</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.2.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16975686" target="_blank" rel="noopener">10.5281/zenodo.16975686</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>biederer-mouse-sc-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></td>
        </tr>
        <tr>
          <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-spatial-visium-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15428115" target="_blank" rel="noopener">10.5281/zenodo.15428115</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16929448" target="_blank" rel="noopener">10.5281/zenodo.16929448</a></td>
        </tr>
        <tr>
          <td><code>alessi-invitro-ms-p-hek293-gtip</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17355407" target="_blank" rel="noopener">10.5281/zenodo.17355407</a></td>
        </tr>
        <tr>
          <td><code>schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17358327" target="_blank" rel="noopener">10.5281/zenodo.17358327</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-spatial-visium-mtg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242087" target="_blank" rel="noopener">10.5281/zenodo.17242087</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-genetics</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242295" target="_blank" rel="noopener">10.5281/zenodo.17242295</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17212215" target="_blank" rel="noopener">10.5281/zenodo.17212215</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149266" target="_blank" rel="noopener">10.5281/zenodo.17149266</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-microglia</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149290" target="_blank" rel="noopener">10.5281/zenodo.17149290</a></td>
        </tr>
        <tr>
          <td><code>sulzer-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17612853" target="_blank" rel="noopener">10.5281/zenodo.17612853</a></td>
        </tr>
        <tr>
          <td><code>cohort-mouse-sc-rnaseq</code></td>
          <td>v1.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17860975" target="_blank" rel="noopener">10.5281/zenodo.17860975</a></td>
        </tr>
        <tr>
          <td><code>schapira-fecal-metagenome-human-baseline</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18353680" target="_blank" rel="noopener">10.5281/zenodo.18353680</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-liver-bulk-rnaseq-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273810" target="_blank" rel="noopener">10.5281/zenodo.18273810</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273802" target="_blank" rel="noopener">10.5281/zenodo.18273802</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273808" target="_blank" rel="noopener">10.5281/zenodo.18273808</a></td>
        </tr>
        <tr>
          <td><code>liddle-human-colon-spatial-cosmx-rna-1000p</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17917788" target="_blank" rel="noopener">10.5281/zenodo.17917788</a></td>
        </tr>
        <tr>
          <td><code>liddle-human-colon-spatial-cosmx-protein-64p</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17917771" target="_blank" rel="noopener">10.5281/zenodo.17917771</a></td>
        </tr>
        <tr>
          <td><code>alessi-mefs-ms-p-vps35-d620n-wt</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476408" target="_blank" rel="noopener">10.5281/zenodo.18476408</a></td>
        </tr>
        <tr>
          <td><code>alessi-mefs-ms-p-vps35-d620n-dmso-mli2</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476410" target="_blank" rel="noopener">10.5281/zenodo.18476410</a></td>
        </tr>
        <tr>
          <td><code>sulzer-fecal-metagenome-fp-spf</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18989559" target="_blank" rel="noopener">10.5281/zenodo.18989559</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-p-lung-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273812" target="_blank" rel="noopener">10.5281/zenodo.18273812</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-plasma-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273818" target="_blank" rel="noopener">10.5281/zenodo.18273818</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-liver-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273822" target="_blank" rel="noopener">10.5281/zenodo.18273822</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-striatum-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273824" target="_blank" rel="noopener">10.5281/zenodo.18273824</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-lung-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273832" target="_blank" rel="noopener">10.5281/zenodo.18273832</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-kidney-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273834" target="_blank" rel="noopener">10.5281/zenodo.18273834</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-l-plasma-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273840" target="_blank" rel="noopener">10.5281/zenodo.18273840</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-l-liver-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273844" target="_blank" rel="noopener">10.5281/zenodo.18273844</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-l-striatum-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273848" target="_blank" rel="noopener">10.5281/zenodo.18273848</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-l-lung-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273852" target="_blank" rel="noopener">10.5281/zenodo.18273852</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-l-kidney-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273858" target="_blank" rel="noopener">10.5281/zenodo.18273858</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-plasma-g2019s-nuc-quant</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273863" target="_blank" rel="noopener">10.5281/zenodo.18273863</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-striatum-g2019s-nuc-quant</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273868" target="_blank" rel="noopener">10.5281/zenodo.18273868</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-midbrain-g2019s-nuc-quant</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273870" target="_blank" rel="noopener">10.5281/zenodo.18273870</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-ms-p-lung-vps35-d620n-wt</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476393" target="_blank" rel="noopener">10.5281/zenodo.18476393</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-ms-p-brain-vps35-d620n-wt</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476398" target="_blank" rel="noopener">10.5281/zenodo.18476398</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476402" target="_blank" rel="noopener">10.5281/zenodo.18476402</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476404" target="_blank" rel="noopener">10.5281/zenodo.18476404</a></td>
        </tr>
        <tr>
          <td><code>voet-pmdbs-sn-multimodal</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18988753" target="_blank" rel="noopener">10.5281/zenodo.18988753</a></td>
        </tr>
        <tr>
          <td><code>voet-pmdbs-sn-atacseq-scalebio-hydrop</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18988743" target="_blank" rel="noopener">10.5281/zenodo.18988743</a></td>
        </tr>
        <tr>
          <td><code>voet-pmdbs-sn-atacseq-scalebio-10x</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18988717" target="_blank" rel="noopener">10.5281/zenodo.18988717</a></td>
        </tr>
        <tr>
          <td><code>voet-pmdbs-sn-atacseq-hydrop</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18988735" target="_blank" rel="noopener">10.5281/zenodo.18988735</a></td>
        </tr>
        <tr>
          <td><code>voet-pmdbs-sn-atacseq-10x</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18988729" target="_blank" rel="noopener">10.5281/zenodo.18988729</a></td>
        </tr>
        <tr>
          <td><code>voet-pmdbs-sn-rnaseq-parsebio</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18988761" target="_blank" rel="noopener">10.5281/zenodo.18988761</a></td>
        </tr>
        <tr>
          <td><code>voet-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18988768" target="_blank" rel="noopener">10.5281/zenodo.18988768</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-midbrain-hybsel</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.19124469" target="_blank" rel="noopener">10.5281/zenodo.19124469</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-lr-wgs</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.19124632" target="_blank" rel="noopener">10.5281/zenodo.19124632</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v4-1-0-1" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v4.1.0</h2>
    <p><strong>Release ID:</strong> <code>v4.1.0</code></p>
    <p><strong>CDE version:</strong> v4.3</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.19740716" target="_blank" rel="noopener">10.5281/zenodo.19740716</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.2</td>
          <td><a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.2</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v3.1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.19876217" target="_blank" rel="noopener">10.5281/zenodo.19876217</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.2.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16975686" target="_blank" rel="noopener">10.5281/zenodo.16975686</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>biederer-mouse-sc-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></td>
        </tr>
        <tr>
          <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-spatial-visium-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15428115" target="_blank" rel="noopener">10.5281/zenodo.15428115</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16929448" target="_blank" rel="noopener">10.5281/zenodo.16929448</a></td>
        </tr>
        <tr>
          <td><code>alessi-invitro-ms-p-hek293-gtip</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17355407" target="_blank" rel="noopener">10.5281/zenodo.17355407</a></td>
        </tr>
        <tr>
          <td><code>schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17358327" target="_blank" rel="noopener">10.5281/zenodo.17358327</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-spatial-visium-mtg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242087" target="_blank" rel="noopener">10.5281/zenodo.17242087</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-genetics</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242295" target="_blank" rel="noopener">10.5281/zenodo.17242295</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17212215" target="_blank" rel="noopener">10.5281/zenodo.17212215</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149266" target="_blank" rel="noopener">10.5281/zenodo.17149266</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-microglia</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149290" target="_blank" rel="noopener">10.5281/zenodo.17149290</a></td>
        </tr>
        <tr>
          <td><code>sulzer-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17612853" target="_blank" rel="noopener">10.5281/zenodo.17612853</a></td>
        </tr>
        <tr>
          <td><code>cohort-mouse-sc-rnaseq</code></td>
          <td>v1.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17860975" target="_blank" rel="noopener">10.5281/zenodo.17860975</a></td>
        </tr>
        <tr>
          <td><code>schapira-fecal-metagenome-human-baseline</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18353680" target="_blank" rel="noopener">10.5281/zenodo.18353680</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-liver-bulk-rnaseq-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273810" target="_blank" rel="noopener">10.5281/zenodo.18273810</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273802" target="_blank" rel="noopener">10.5281/zenodo.18273802</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273808" target="_blank" rel="noopener">10.5281/zenodo.18273808</a></td>
        </tr>
        <tr>
          <td><code>liddle-human-colon-spatial-cosmx-rna-1000p</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17917788" target="_blank" rel="noopener">10.5281/zenodo.17917788</a></td>
        </tr>
        <tr>
          <td><code>liddle-human-colon-spatial-cosmx-protein-64p</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17917771" target="_blank" rel="noopener">10.5281/zenodo.17917771</a></td>
        </tr>
        <tr>
          <td><code>alessi-mefs-ms-p-vps35-d620n-wt</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476408" target="_blank" rel="noopener">10.5281/zenodo.18476408</a></td>
        </tr>
        <tr>
          <td><code>alessi-mefs-ms-p-vps35-d620n-dmso-mli2</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476410" target="_blank" rel="noopener">10.5281/zenodo.18476410</a></td>
        </tr>
        <tr>
          <td><code>sulzer-fecal-metagenome-fp-spf</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18989559" target="_blank" rel="noopener">10.5281/zenodo.18989559</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-p-lung-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273812" target="_blank" rel="noopener">10.5281/zenodo.18273812</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-plasma-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273818" target="_blank" rel="noopener">10.5281/zenodo.18273818</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-liver-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273822" target="_blank" rel="noopener">10.5281/zenodo.18273822</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-striatum-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273824" target="_blank" rel="noopener">10.5281/zenodo.18273824</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-lung-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273832" target="_blank" rel="noopener">10.5281/zenodo.18273832</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-kidney-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273834" target="_blank" rel="noopener">10.5281/zenodo.18273834</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-l-plasma-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273840" target="_blank" rel="noopener">10.5281/zenodo.18273840</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-l-liver-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273844" target="_blank" rel="noopener">10.5281/zenodo.18273844</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-l-striatum-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273848" target="_blank" rel="noopener">10.5281/zenodo.18273848</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-l-lung-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273852" target="_blank" rel="noopener">10.5281/zenodo.18273852</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-l-kidney-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273858" target="_blank" rel="noopener">10.5281/zenodo.18273858</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-plasma-g2019s-nuc-quant</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273863" target="_blank" rel="noopener">10.5281/zenodo.18273863</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-striatum-g2019s-nuc-quant</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273868" target="_blank" rel="noopener">10.5281/zenodo.18273868</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-ms-mb-midbrain-g2019s-nuc-quant</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273870" target="_blank" rel="noopener">10.5281/zenodo.18273870</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-ms-p-lung-vps35-d620n-wt</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476393" target="_blank" rel="noopener">10.5281/zenodo.18476393</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-ms-p-brain-vps35-d620n-wt</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476398" target="_blank" rel="noopener">10.5281/zenodo.18476398</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476402" target="_blank" rel="noopener">10.5281/zenodo.18476402</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476404" target="_blank" rel="noopener">10.5281/zenodo.18476404</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v4-0-2-2" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v4.0.2</h2>
    <p><strong>Release ID:</strong> <code>v4.0.2</code></p>
    <p><strong>CDE version:</strong> v4.2</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.19289362" target="_blank" rel="noopener">10.5281/zenodo.19289362</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.2</td>
          <td><a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.2</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v3.1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.19876217" target="_blank" rel="noopener">10.5281/zenodo.19876217</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.2.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16975686" target="_blank" rel="noopener">10.5281/zenodo.16975686</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>biederer-mouse-sc-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></td>
        </tr>
        <tr>
          <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-spatial-visium-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15428115" target="_blank" rel="noopener">10.5281/zenodo.15428115</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16929448" target="_blank" rel="noopener">10.5281/zenodo.16929448</a></td>
        </tr>
        <tr>
          <td><code>alessi-invitro-ms-p-hek293-gtip</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17355407" target="_blank" rel="noopener">10.5281/zenodo.17355407</a></td>
        </tr>
        <tr>
          <td><code>schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17358327" target="_blank" rel="noopener">10.5281/zenodo.17358327</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-spatial-visium-mtg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242087" target="_blank" rel="noopener">10.5281/zenodo.17242087</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-genetics</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242295" target="_blank" rel="noopener">10.5281/zenodo.17242295</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17212215" target="_blank" rel="noopener">10.5281/zenodo.17212215</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149266" target="_blank" rel="noopener">10.5281/zenodo.17149266</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-microglia</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149290" target="_blank" rel="noopener">10.5281/zenodo.17149290</a></td>
        </tr>
        <tr>
          <td><code>sulzer-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17612853" target="_blank" rel="noopener">10.5281/zenodo.17612853</a></td>
        </tr>
        <tr>
          <td><code>cohort-mouse-sc-rnaseq</code></td>
          <td>v1.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17860975" target="_blank" rel="noopener">10.5281/zenodo.17860975</a></td>
        </tr>
        <tr>
          <td><code>schapira-fecal-metagenome-human-baseline</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18353680" target="_blank" rel="noopener">10.5281/zenodo.18353680</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-liver-bulk-rnaseq-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273810" target="_blank" rel="noopener">10.5281/zenodo.18273810</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273802" target="_blank" rel="noopener">10.5281/zenodo.18273802</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273808" target="_blank" rel="noopener">10.5281/zenodo.18273808</a></td>
        </tr>
        <tr>
          <td><code>liddle-human-colon-spatial-cosmx-rna-1000p</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17917788" target="_blank" rel="noopener">10.5281/zenodo.17917788</a></td>
        </tr>
        <tr>
          <td><code>liddle-human-colon-spatial-cosmx-protein-64p</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17917771" target="_blank" rel="noopener">10.5281/zenodo.17917771</a></td>
        </tr>
        <tr>
          <td><code>alessi-mefs-ms-p-vps35-d620n-wt</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476408" target="_blank" rel="noopener">10.5281/zenodo.18476408</a></td>
        </tr>
        <tr>
          <td><code>alessi-mefs-ms-p-vps35-d620n-dmso-mli2</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18476410" target="_blank" rel="noopener">10.5281/zenodo.18476410</a></td>
        </tr>
        <tr>
          <td><code>sulzer-fecal-metagenome-fp-spf</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18989559" target="_blank" rel="noopener">10.5281/zenodo.18989559</a></td>
        </tr>
        <tr>
          <td><code>alessi-invitro-ms-p-hek293-gtip</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17355407" target="_blank" rel="noopener">10.5281/zenodo.17355407</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v4-0-2-3" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v4.0.2</h2>
    <p><strong>Release ID:</strong> <code>v4.0.2</code></p>
    <p><strong>CDE version:</strong> TBD</p>
    <p><strong>Release DOI:</strong> TBD</p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3">No datasets listed for this release.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v4-0-1-4" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v4.0.1</h2>
    <p><strong>Release ID:</strong> <code>v4.0.1</code></p>
    <p><strong>CDE version:</strong> v4.1</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18780122" target="_blank" rel="noopener">10.5281/zenodo.18780122</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.2</td>
          <td><a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.2</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v3.1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.19876217" target="_blank" rel="noopener">10.5281/zenodo.19876217</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.2.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16975686" target="_blank" rel="noopener">10.5281/zenodo.16975686</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>biederer-mouse-sc-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></td>
        </tr>
        <tr>
          <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-spatial-visium-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15428115" target="_blank" rel="noopener">10.5281/zenodo.15428115</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16929448" target="_blank" rel="noopener">10.5281/zenodo.16929448</a></td>
        </tr>
        <tr>
          <td><code>alessi-invitro-ms-p-hek293-gtip</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17355407" target="_blank" rel="noopener">10.5281/zenodo.17355407</a></td>
        </tr>
        <tr>
          <td><code>schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17358327" target="_blank" rel="noopener">10.5281/zenodo.17358327</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-spatial-visium-mtg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242087" target="_blank" rel="noopener">10.5281/zenodo.17242087</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-genetics</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242295" target="_blank" rel="noopener">10.5281/zenodo.17242295</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17212215" target="_blank" rel="noopener">10.5281/zenodo.17212215</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149266" target="_blank" rel="noopener">10.5281/zenodo.17149266</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-microglia</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149290" target="_blank" rel="noopener">10.5281/zenodo.17149290</a></td>
        </tr>
        <tr>
          <td><code>sulzer-pmdbs-sn-rnaseq</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.17612853" target="_blank" rel="noopener">10.5281/zenodo.17612853</a></td>
        </tr>
        <tr>
          <td><code>cohort-mouse-sc-rnaseq</code></td>
          <td>v1.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17860975" target="_blank" rel="noopener">10.5281/zenodo.17860975</a></td>
        </tr>
        <tr>
          <td><code>schapira-fecal-metagenome-human-baseline</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18353680" target="_blank" rel="noopener">10.5281/zenodo.18353680</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-liver-bulk-rnaseq-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273810" target="_blank" rel="noopener">10.5281/zenodo.18273810</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273802" target="_blank" rel="noopener">10.5281/zenodo.18273802</a></td>
        </tr>
        <tr>
          <td><code>lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.18273808" target="_blank" rel="noopener">10.5281/zenodo.18273808</a></td>
        </tr>
        <tr>
          <td><code>liddle-human-colon-spatial-cosmx-rna-1000p</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17917788" target="_blank" rel="noopener">10.5281/zenodo.17917788</a></td>
        </tr>
        <tr>
          <td><code>liddle-human-colon-spatial-cosmx-protein-64p</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17917771" target="_blank" rel="noopener">10.5281/zenodo.17917771</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v4-0-0-5" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v4.0.0</h2>
    <p><strong>Release ID:</strong> <code>v4.0.0</code></p>
    <p><strong>CDE version:</strong> v3.3</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17834620" target="_blank" rel="noopener">10.5281/zenodo.17834620</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v3.1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17860778" target="_blank" rel="noopener">10.5281/zenodo.17860778</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.2.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17860841" target="_blank" rel="noopener">10.5281/zenodo.17860841</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>biederer-mouse-sc-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></td>
        </tr>
        <tr>
          <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-spatial-visium-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15428115" target="_blank" rel="noopener">10.5281/zenodo.15428115</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16929448" target="_blank" rel="noopener">10.5281/zenodo.16929448</a></td>
        </tr>
        <tr>
          <td><code>alessi-invitro-ms-p-hek293-gtip</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></td>
        </tr>
        <tr>
          <td><code>schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17358327" target="_blank" rel="noopener">10.5281/zenodo.17358327</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-spatial-visium-mtg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242087" target="_blank" rel="noopener">10.5281/zenodo.17242087</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-genetics</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242295" target="_blank" rel="noopener">10.5281/zenodo.17242295</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17212215" target="_blank" rel="noopener">10.5281/zenodo.17212215</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149266" target="_blank" rel="noopener">10.5281/zenodo.17149266</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-microglia</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149290" target="_blank" rel="noopener">10.5281/zenodo.17149290</a></td>
        </tr>
        <tr>
          <td><code>sulzer-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17612853" target="_blank" rel="noopener">10.5281/zenodo.17612853</a></td>
        </tr>
        <tr>
          <td><code>cohort-mouse-sc-rnaseq</code></td>
          <td>v1.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17860975" target="_blank" rel="noopener">10.5281/zenodo.17860975</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v4-0-0-6" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v4.0.0</h2>
    <p><strong>Release ID:</strong> <code>v4.0.0</code></p>
    <p><strong>CDE version:</strong> TBD</p>
    <p><strong>Release DOI:</strong> TBD</p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3">No datasets listed for this release.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v3-0-2-7" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v3.0.2</h2>
    <p><strong>Release ID:</strong> <code>v3.0.2</code></p>
    <p><strong>CDE version:</strong> v3.2</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17727566" target="_blank" rel="noopener">10.5281/zenodo.17727566</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v3.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16979638" target="_blank" rel="noopener">10.5281/zenodo.16979638</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16975686" target="_blank" rel="noopener">10.5281/zenodo.16975686</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>biederer-mouse-sc-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></td>
        </tr>
        <tr>
          <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-spatial-visium-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15428115" target="_blank" rel="noopener">10.5281/zenodo.15428115</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16929448" target="_blank" rel="noopener">10.5281/zenodo.16929448</a></td>
        </tr>
        <tr>
          <td><code>alessi-invitro-ms-p-hek293-gtip</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></td>
        </tr>
        <tr>
          <td><code>schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17358327" target="_blank" rel="noopener">10.5281/zenodo.17358327</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-spatial-visium-mtg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242087" target="_blank" rel="noopener">10.5281/zenodo.17242087</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-genetics</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242295" target="_blank" rel="noopener">10.5281/zenodo.17242295</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17212215" target="_blank" rel="noopener">10.5281/zenodo.17212215</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149266" target="_blank" rel="noopener">10.5281/zenodo.17149266</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-invitro-bulk-rnaseq-microglia</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17149290" target="_blank" rel="noopener">10.5281/zenodo.17149290</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v3-0-2-8" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v3.0.2</h2>
    <p><strong>Release ID:</strong> <code>v3.0.2</code></p>
    <p><strong>CDE version:</strong> TBD</p>
    <p><strong>Release DOI:</strong> TBD</p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3">No datasets listed for this release.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v3-0-1-9" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v3.0.1</h2>
    <p><strong>Release ID:</strong> <code>v3.0.1</code></p>
    <p><strong>CDE version:</strong> v3.2</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17497025" target="_blank" rel="noopener">10.5281/zenodo.17497025</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.1</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v3.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16979638" target="_blank" rel="noopener">10.5281/zenodo.16979638</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16975686" target="_blank" rel="noopener">10.5281/zenodo.16975686</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>biederer-mouse-sc-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></td>
        </tr>
        <tr>
          <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-spatial-visium-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15428115" target="_blank" rel="noopener">10.5281/zenodo.15428115</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16929448" target="_blank" rel="noopener">10.5281/zenodo.16929448</a></td>
        </tr>
        <tr>
          <td><code>alessi-invitro-ms-p-hek293-gtip</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></td>
        </tr>
        <tr>
          <td><code>schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17358327" target="_blank" rel="noopener">10.5281/zenodo.17358327</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-spatial-visium-mtg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242087" target="_blank" rel="noopener">10.5281/zenodo.17242087</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-genetics</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17242295" target="_blank" rel="noopener">10.5281/zenodo.17242295</a></td>
        </tr>
        <tr>
          <td><code>alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.17212215" target="_blank" rel="noopener">10.5281/zenodo.17212215</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v3-0-1-10" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v3.0.1</h2>
    <p><strong>Release ID:</strong> <code>v3.0.1</code></p>
    <p><strong>CDE version:</strong> TBD</p>
    <p><strong>Release DOI:</strong> TBD</p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3">No datasets listed for this release.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v3-0-0-11" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v3.0.0</h2>
    <p><strong>Release ID:</strong> <code>v3.0.0</code></p>
    <p><strong>CDE version:</strong> v3.2</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16975257" target="_blank" rel="noopener">10.5281/zenodo.16975257</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885831" target="_blank" rel="noopener">10.5281/zenodo.16885831</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v3.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16979638" target="_blank" rel="noopener">10.5281/zenodo.16979638</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16975686" target="_blank" rel="noopener">10.5281/zenodo.16975686</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>biederer-mouse-sc-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></td>
        </tr>
        <tr>
          <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-spatial-visium-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15428115" target="_blank" rel="noopener">10.5281/zenodo.15428115</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16929448" target="_blank" rel="noopener">10.5281/zenodo.16929448</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v3-0-0-12" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v3.0.0</h2>
    <p><strong>Release ID:</strong> <code>v3.0.0</code></p>
    <p><strong>CDE version:</strong> TBD</p>
    <p><strong>Release DOI:</strong> TBD</p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3">No datasets listed for this release.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v2-0-3-13" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v2.0.3</h2>
    <p><strong>Release ID:</strong> <code>v2.0.3</code></p>
    <p><strong>CDE version:</strong> v3.0</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15831618" target="_blank" rel="noopener">10.5281/zenodo.15831618</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885831" target="_blank" rel="noopener">10.5281/zenodo.16885831</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v2.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.14373047" target="_blank" rel="noopener">10.5281/zenodo.14373047</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.14373343" target="_blank" rel="noopener">10.5281/zenodo.14373343</a></td>
        </tr>
        <tr>
          <td><code>biederer-mouse-sc-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></td>
        </tr>
        <tr>
          <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-spatial-visium-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15428115" target="_blank" rel="noopener">10.5281/zenodo.15428115</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v2-0-3-14" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v2.0.3</h2>
    <p><strong>Release ID:</strong> <code>v2.0.3</code></p>
    <p><strong>CDE version:</strong> TBD</p>
    <p><strong>Release DOI:</strong> TBD</p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3">No datasets listed for this release.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v2-0-2-15" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v2.0.2</h2>
    <p><strong>Release ID:</strong> <code>v2.0.2</code></p>
    <p><strong>CDE version:</strong> v3.0</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15831618" target="_blank" rel="noopener">10.5281/zenodo.15831618</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885831" target="_blank" rel="noopener">10.5281/zenodo.16885831</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v2.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.14373047" target="_blank" rel="noopener">10.5281/zenodo.14373047</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.14373343" target="_blank" rel="noopener">10.5281/zenodo.14373343</a></td>
        </tr>
        <tr>
          <td><code>biederer-mouse-sc-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></td>
        </tr>
        <tr>
          <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></td>
        </tr>
        <tr>
          <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v2-0-2-16" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v2.0.2</h2>
    <p><strong>Release ID:</strong> <code>v2.0.2</code></p>
    <p><strong>CDE version:</strong> TBD</p>
    <p><strong>Release DOI:</strong> TBD</p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3">No datasets listed for this release.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v2-0-1-17" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v2.0.1</h2>
    <p><strong>Release ID:</strong> <code>v2.0.1</code></p>
    <p><strong>CDE version:</strong> v3.0</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15831558" target="_blank" rel="noopener">10.5281/zenodo.15831558</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v2.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885831" target="_blank" rel="noopener">10.5281/zenodo.16885831</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v2.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.14373047" target="_blank" rel="noopener">10.5281/zenodo.14373047</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.14373343" target="_blank" rel="noopener">10.5281/zenodo.14373343</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v2-0-1-18" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v2.0.1</h2>
    <p><strong>Release ID:</strong> <code>v2.0.1</code></p>
    <p><strong>CDE version:</strong> TBD</p>
    <p><strong>Release DOI:</strong> TBD</p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3">No datasets listed for this release.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v2-0-0-19" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v2.0.0</h2>
    <p><strong>Release ID:</strong> <code>v2.0.0</code></p>
    <p><strong>CDE version:</strong> v3.0</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.14270014" target="_blank" rel="noopener">10.5281/zenodo.14270014</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885831" target="_blank" rel="noopener">10.5281/zenodo.16885831</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></td>
        </tr>
        <tr>
          <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></td>
        </tr>
        <tr>
          <td><code>wood-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v2.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.14373048" target="_blank" rel="noopener">10.5281/zenodo.14373048</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
          <td>v1.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.14373344" target="_blank" rel="noopener">10.5281/zenodo.14373344</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v2-0-0-20" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v2.0.0</h2>
    <p><strong>Release ID:</strong> <code>v2.0.0</code></p>
    <p><strong>CDE version:</strong> TBD</p>
    <p><strong>Release DOI:</strong> TBD</p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3">No datasets listed for this release.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v1-0-0-21" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v1.0.0</h2>
    <p><strong>Release ID:</strong> <code>v1.0.0</code></p>
    <p><strong>CDE version:</strong> v2.1</p>
    <p><strong>Release DOI:</strong> <a href="https://doi.org/10.5281/zenodo.11585274" target="_blank" rel="noopener">10.5281/zenodo.11585274</a></p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></td>
        </tr>
        <tr>
          <td><code>lee-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></td>
        </tr>
        <tr>
          <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></td>
        </tr>
        <tr>
          <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
          <td>v1.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.16885831" target="_blank" rel="noopener">10.5281/zenodo.16885831</a></td>
        </tr>
        <tr>
          <td><code>cohort-pmdbs-sc-rnaseq</code></td>
          <td>v1.0.0</td>
          <td><a href="https://doi.org/10.5281/zenodo.14373047" target="_blank" rel="noopener">10.5281/zenodo.14373047</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
<div id="release-modal-v1-0-0-22" class="release-modal">
  <div class="release-modal-content">
    <span class="release-modal-close" data-close="true">&times;</span>
    <h2>CRN Cloud Release v1.0.0</h2>
    <p><strong>Release ID:</strong> <code>v1.0.0</code></p>
    <p><strong>CDE version:</strong> TBD</p>
    <p><strong>Release DOI:</strong> TBD</p>
    <h3>Datasets in this release</h3>
    <table class="release-table">
      <thead>
        <tr>
          <th>Dataset</th>
          <th>Dataset version</th>
          <th>DOI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3">No datasets listed for this release.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>