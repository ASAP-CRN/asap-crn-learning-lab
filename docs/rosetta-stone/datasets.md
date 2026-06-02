# CRN Cloud Datasets

Use this table to find dataset records, review versioning, and locate related release information.

<div class="dataset-filters">
  <input id="datasetSearch" class="dataset-search" type="text" placeholder="Filter by dataset, title, collection, tag, release, DOI, CDE version, or bucket path...">
  <select id="tagFilter" class="tag-filter">
<option value="">All tags</option>
<option value="alessi">alessi</option>
<option value="biederer">biederer</option>
<option value="brain">brain</option>
<option value="bulk-rnaseq">bulk-rnaseq</option>
<option value="cohort">cohort</option>
<option value="cragg">cragg</option>
<option value="edwards">edwards</option>
<option value="fecal-metagenome">fecal-metagenome</option>
<option value="hafler">hafler</option>
<option value="hardy">hardy</option>
<option value="human-colon">human-colon</option>
<option value="invitro">invitro</option>
<option value="invitro-bulk-rnaseq">invitro-bulk-rnaseq</option>
<option value="jakobsson">jakobsson</option>
<option value="kidney">kidney</option>
<option value="lee">lee</option>
<option value="liddle">liddle</option>
<option value="liver">liver</option>
<option value="lr-wgs">lr-wgs</option>
<option value="lung">lung</option>
<option value="mefs">mefs</option>
<option value="midbrain">midbrain</option>
<option value="mouse">mouse</option>
<option value="mouse-other">mouse-other</option>
<option value="mouse-sc-rnaseq">mouse-sc-rnaseq</option>
<option value="mouse-spatial-rnaseq">mouse-spatial-rnaseq</option>
<option value="ms-p">ms-p</option>
<option value="other-mouse">other-mouse</option>
<option value="other-pmdbs">other-pmdbs</option>
<option value="plasma">plasma</option>
<option value="pmdbs">pmdbs</option>
<option value="pmdbs-bulk-rnaseq">pmdbs-bulk-rnaseq</option>
<option value="pmdbs-genetics">pmdbs-genetics</option>
<option value="pmdbs-other">pmdbs-other</option>
<option value="pmdbs-sc-rnaseq">pmdbs-sc-rnaseq</option>
<option value="pmdbs-spatial-rnaseq">pmdbs-spatial-rnaseq</option>
<option value="proteomics">proteomics</option>
<option value="schapira">schapira</option>
<option value="scherzer">scherzer</option>
<option value="schlossmacher">schlossmacher</option>
<option value="sn-atacseq">sn-atacseq</option>
<option value="sn-multimodal">sn-multimodal</option>
<option value="sn-rnaseq">sn-rnaseq</option>
<option value="spatial-cosmx">spatial-cosmx</option>
<option value="striatum">striatum</option>
<option value="sulzer">sulzer</option>
<option value="voet">voet</option>
<option value="wood">wood</option>
  </select>
</div>

<p id="datasetCount" class="dataset-count"></p>

<style>
.md-grid {
  max-width: 72rem;
}
.dataset-filters {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  margin: 1rem 0 0.5rem 0;
}
.dataset-search {
  flex: 1;
  padding: 0.65rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.45rem;
  font-size: 0.9rem;
}
.tag-filter {
  min-width: 180px;
  padding: 0.65rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.45rem;
  font-size: 0.9rem;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
}
@media (max-width: 700px) {
  .dataset-filters {
    flex-direction: column;
    align-items: stretch;
  }
  .tag-filter {
    width: 100%;
  }
}
.dataset-count {
  margin: 0 0 1rem 0;
  color: var(--md-default-fg-color--light);
}
.dataset-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.78rem;
  table-layout: fixed;
}
.dataset-table th, .dataset-table td {
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
  padding: 0.42rem;
  text-align: left;
  vertical-align: top;
  word-break: break-word;
}
.dataset-table th {
  font-weight: 700;
}
.dataset-table th:nth-child(1), .dataset-table td:nth-child(1) {
  width: 24%;
}
.dataset-table th:nth-child(2), .dataset-table td:nth-child(2) {
  width: 34%;
}
.dataset-table th:nth-child(3), .dataset-table td:nth-child(3) {
  width: 14%;
}
.dataset-table th:nth-child(4), .dataset-table td:nth-child(4) {
  width: 10%;
}
.dataset-table th:nth-child(5), .dataset-table td:nth-child(5) {
  width: 10%;
}
.dataset-table th:nth-child(6), .dataset-table td:nth-child(6) {
  width: 8%;
}
.dataset-toggle {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.35rem;
  padding: 0.25rem 0.45rem;
  background: var(--md-default-bg-color);
  cursor: pointer;
  font-size: 0.75rem;
}
.dataset-toggle:hover {
  border-color: var(--md-accent-fg-color);
}
.dataset-detail-row {
  display: none;
}
.dataset-detail {
  padding: 0.75rem;
  border-left: 3px solid var(--md-accent-fg-color);
  background: var(--md-code-bg-color);
}
.dataset-detail h4 {
  margin-top: 0.75rem;
  margin-bottom: 0.35rem;
}
.tag-pill {
  display: inline-block;
  padding: 0.12rem 0.4rem;
  margin: 0.1rem 0.15rem 0.1rem 0;
  border-radius: 999px;
  background: var(--md-default-bg-color);
  font-size: 0.72rem;
  white-space: nowrap;
}
.mini-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
}
.mini-table th, .mini-table td {
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
  padding: 0.4rem;
  text-align: left;
  vertical-align: top;
}
</style>

<table class="dataset-table" id="datasetTable">
  <thead>
    <tr>
      <th>Dataset</th>
      <th>Title</th>
      <th>Collection</th>
      <th>Current version</th>
      <th>Latest release</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr class="dataset-row" data-detail="dataset-detail-alessi-invitro-ms-p-hek293-gtip-0" data-search="alessi-invitro-ms-p-hek293-gtip golgi-ip, a tool for multimodal analysis of golgi molecular content quantitative dia-based proteomic analysis of golgi-ip in hek293 cells. the data set contains six replicates of golgitag-ip, control-ip, golgitag whole cell extract and control cells whole cell extract. the mass spectrometry data is acquired using variable data independent acquisition (vdia) on an orbitrap exploris 480 mass spectrometer. database searches performed against human uniprot database using spectronaut search algorithm. na cc-by-4.0 10.5281/zenodo.17355407 alessi invitro ms-p proteomics invitro ms-p proteomics alessi gs://asap-raw-team-alessi-invitro-ms-p-hek293-gtip gs://asap-dev-team-alessi-invitro-ms-p-hek293-gtip gs://asap-uat-team-alessi-invitro-ms-p-hek293-gtip gs://asap-curated-team-alessi-invitro-ms-p-hek293-gtip v3.0.1 v4.0.0 v4.0.2 v3.0.1 v1.0 v3.3 v4.0.0 v1.0 v3.3 v4.0.2 v1.1 v4.2" data-tags="alessi||invitro||ms-p||proteomics">
      <td><code>alessi-invitro-ms-p-hek293-gtip</code></td>
      <td>Golgi-IP, a tool for multimodal analysis of Golgi molecular content</td>
      <td>NA</td>
      <td>v1.1</td>
      <td>v4.0.2</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-alessi-invitro-ms-p-hek293-gtip-0">View</button></td>
    </tr>
    <tr id="dataset-detail-alessi-invitro-ms-p-hek293-gtip-0" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Golgi-IP, a tool for multimodal analysis of Golgi molecular content</h3>
          <p><strong>Dataset ID:</strong> <code>alessi-invitro-ms-p-hek293-gtip</code></p>
          <p><strong>Description:</strong> Quantitative DIA-based proteomic analysis of Golgi-IP in HEK293 cells. The data set contains six replicates of GolgiTAG-IP, Control-IP, GolgiTAG whole cell extract and Control cells whole cell extract. The mass spectrometry data is acquired using variable data independent acquisition (vDIA) on an Orbitrap Exploris 480 mass spectrometer. Database searches performed against Human Uniprot database using Spectronaut search algorithm.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.1</p>
          <p><strong>Latest release:</strong> v4.0.2</p>
          <p><strong>Latest CDE version:</strong> v4.2</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17355407" target="_blank" rel="noopener">10.5281/zenodo.17355407</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">alessi</span> <span class="tag-pill">invitro</span> <span class="tag-pill">ms-p</span> <span class="tag-pill">proteomics</span></p>
          <p><strong>Keywords:</strong> invitro, ms-p, proteomics, alessi</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.2</td>
                <td>v1.1</td>
                <td>v4.2</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.1</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-alessi-invitro-ms-p-hek293-gtip</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-alessi-invitro-ms-p-hek293-gtip</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-alessi-invitro-ms-p-hek293-gtip</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-alessi-invitro-ms-p-hek293-gtip</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-alessi-mefs-ms-p-vps35-d620n-dmso-mli2-1" data-search="alessi-mefs-ms-p-vps35-d620n-dmso-mli2 quantitative dia-based proteomic analysis of lysosomes (lyso-ip) from vps35[d620n] mouse embryonic fibroblasts (mefs) with lrrk2 inhibition. quantitative dia-based proteomic analysis of isolated lysosomes (lyso-ip) and whole-cell extracts (wcl) from vps35[d620n] knock-in mefs. the dataset includes six biological replicates comparing cells treated with the lrrk2 inhibitor mli-2 (100 nm, 2 h) against dmso vehicle controls. expression of the 3xha-tmem192 lysosomal tag was determined by genotyping pcr and verified via anti-ha immunoblotting. data acquired on an orbitrap exploris 480 and processed using dia-nn 1.8.1. na cc-by-4.0 10.5281/zenodo.18476410 alessi mefs ms-p mefs ms-p alessi gs://asap-raw-team-alessi-mefs-ms-p-vps35-d620n-dmso-mli2 gs://asap-dev-team-alessi-mefs-ms-p-vps35-d620n-dmso-mli2 gs://asap-uat-team-alessi-mefs-ms-p-vps35-d620n-dmso-mli2 gs://asap-curated-team-alessi-mefs-ms-p-vps35-d620n-dmso-mli2 v4.0.2 v4.0.2 v1.0 v4.3" data-tags="alessi||mefs||ms-p">
      <td><code>alessi-mefs-ms-p-vps35-d620n-dmso-mli2</code></td>
      <td>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Embryonic Fibroblasts (MEFs) with LRRK2 inhibition.</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.2</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-alessi-mefs-ms-p-vps35-d620n-dmso-mli2-1">View</button></td>
    </tr>
    <tr id="dataset-detail-alessi-mefs-ms-p-vps35-d620n-dmso-mli2-1" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Embryonic Fibroblasts (MEFs) with LRRK2 inhibition.</h3>
          <p><strong>Dataset ID:</strong> <code>alessi-mefs-ms-p-vps35-d620n-dmso-mli2</code></p>
          <p><strong>Description:</strong> Quantitative DIA-based proteomic analysis of isolated lysosomes (Lyso-IP) and whole-cell extracts (WCL) from VPS35[D620N] knock-in MEFs. The dataset includes six biological replicates comparing cells treated with the LRRK2 inhibitor MLi-2 (100 nM, 2 h) against DMSO vehicle controls. Expression of the 3XHA-TMEM192 lysosomal tag was determined by genotyping PCR and verified via anti-HA immunoblotting. Data acquired on an Orbitrap Exploris 480 and processed using DIA-NN 1.8.1.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.2</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18476410" target="_blank" rel="noopener">10.5281/zenodo.18476410</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">alessi</span> <span class="tag-pill">mefs</span> <span class="tag-pill">ms-p</span></p>
          <p><strong>Keywords:</strong> mefs, ms-p, alessi</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.2</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-alessi-mefs-ms-p-vps35-d620n-dmso-mli2</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-alessi-mefs-ms-p-vps35-d620n-dmso-mli2</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-alessi-mefs-ms-p-vps35-d620n-dmso-mli2</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-alessi-mefs-ms-p-vps35-d620n-dmso-mli2</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-alessi-mefs-ms-p-vps35-d620n-wt-2" data-search="alessi-mefs-ms-p-vps35-d620n-wt quantitative dia-based proteomic analysis of lysosomes (lyso-ip) from vps35[d620n] mouse embryonic fibroblasts (mefs) with lrrk2 inhibition. quantitative dia-based proteomic analysis of isolated lysosomes (lyso-ip) and whole-cell extracts (wcl) from vps35[d620n] knock-in mefs. the dataset includes six biological replicates comparing cells treated with the lrrk2 inhibitor mli-2 (100 nm, 2 h) against dmso vehicle controls. expression of the 3xha-tmem192 lysosomal tag was determined by genotyping pcr and verified via anti-ha immunoblotting. data acquired on an orbitrap exploris 480 and processed using dia-nn 1.8.1. na cc-by-4.0 10.5281/zenodo.18476408 alessi mefs ms-p mefs ms-p alessi gs://asap-raw-team-alessi-mefs-ms-p-vps35-d620n-wt gs://asap-dev-team-alessi-mefs-ms-p-vps35-d620n-wt gs://asap-uat-team-alessi-mefs-ms-p-vps35-d620n-wt gs://asap-curated-team-alessi-mefs-ms-p-vps35-d620n-wt v4.0.2 v4.0.2 v1.0 v4.3" data-tags="alessi||mefs||ms-p">
      <td><code>alessi-mefs-ms-p-vps35-d620n-wt</code></td>
      <td>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Embryonic Fibroblasts (MEFs) with LRRK2 inhibition.</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.2</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-alessi-mefs-ms-p-vps35-d620n-wt-2">View</button></td>
    </tr>
    <tr id="dataset-detail-alessi-mefs-ms-p-vps35-d620n-wt-2" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Embryonic Fibroblasts (MEFs) with LRRK2 inhibition.</h3>
          <p><strong>Dataset ID:</strong> <code>alessi-mefs-ms-p-vps35-d620n-wt</code></p>
          <p><strong>Description:</strong> Quantitative DIA-based proteomic analysis of isolated lysosomes (Lyso-IP) and whole-cell extracts (WCL) from VPS35[D620N] knock-in MEFs. The dataset includes six biological replicates comparing cells treated with the LRRK2 inhibitor MLi-2 (100 nM, 2 h) against DMSO vehicle controls. Expression of the 3XHA-TMEM192 lysosomal tag was determined by genotyping PCR and verified via anti-HA immunoblotting. Data acquired on an Orbitrap Exploris 480 and processed using DIA-NN 1.8.1.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.2</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18476408" target="_blank" rel="noopener">10.5281/zenodo.18476408</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">alessi</span> <span class="tag-pill">mefs</span> <span class="tag-pill">ms-p</span></p>
          <p><strong>Keywords:</strong> mefs, ms-p, alessi</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.2</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-alessi-mefs-ms-p-vps35-d620n-wt</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-alessi-mefs-ms-p-vps35-d620n-wt</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-alessi-mefs-ms-p-vps35-d620n-wt</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-alessi-mefs-ms-p-vps35-d620n-wt</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2-3" data-search="alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2 quantitative dia-based proteomic analysis of lysosomes (lyso-ip) from vps35[d620n] mouse brain with lrrk2 inhibition. proteomic analysis of lysosomes isolated from the brain tissue of vps35[d620n] mice treated in vivo with mli-2 (100 mg/kg via oral gavage, 2 h). tag expression was determined by genotyping pcr and brain lysate immunoblotting. data acquired on an orbitrap exploris 480 and processed using dia-nn 1.8.1. na cc-by-4.0 10.5281/zenodo.18476402 alessi brain mouse mouse brain alessi gs://asap-raw-team-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2 gs://asap-dev-team-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2 gs://asap-uat-team-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2 gs://asap-curated-team-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2 v4.1.0 v4.1.0 v1.0 v4.3" data-tags="alessi||brain||mouse">
      <td><code>alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2</code></td>
      <td>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Brain with LRRK2 inhibition.</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2-3">View</button></td>
    </tr>
    <tr id="dataset-detail-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2-3" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Brain with LRRK2 inhibition.</h3>
          <p><strong>Dataset ID:</strong> <code>alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2</code></p>
          <p><strong>Description:</strong> Proteomic analysis of lysosomes isolated from the brain tissue of VPS35[D620N] mice treated in vivo with MLi-2 (100 mg/kg via oral gavage, 2 h). Tag expression was determined by genotyping PCR and brain lysate immunoblotting. Data acquired on an Orbitrap Exploris 480 and processed using DIA-NN 1.8.1.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18476402" target="_blank" rel="noopener">10.5281/zenodo.18476402</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">alessi</span> <span class="tag-pill">brain</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, brain, alessi</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-alessi-mouse-ms-p-brain-vps35-d620n-dmso-mli2</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-alessi-mouse-ms-p-brain-vps35-d620n-wt-4" data-search="alessi-mouse-ms-p-brain-vps35-d620n-wt quantitative dia-based proteomic analysis of lysosomes (lyso-ip) from vps35[d620n] mouse brain. proteomic characterization of brain lysosomes comparing wt and vps35[d620n] mutant mice. tissue was processed via glass-teflon homogenization and 3-minute lyso-ip. data acquired on an orbitrap exploris 480 and processed using dia-nn 1.8.1. na cc-by-4.0 10.5281/zenodo.18476398 alessi brain mouse mouse brain alessi gs://asap-raw-team-alessi-mouse-ms-p-brain-vps35-d620n-wt gs://asap-dev-team-alessi-mouse-ms-p-brain-vps35-d620n-wt gs://asap-uat-team-alessi-mouse-ms-p-brain-vps35-d620n-wt gs://asap-curated-team-alessi-mouse-ms-p-brain-vps35-d620n-wt v4.1.0 v4.1.0 v1.0 v4.3" data-tags="alessi||brain||mouse">
      <td><code>alessi-mouse-ms-p-brain-vps35-d620n-wt</code></td>
      <td>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Brain.</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-alessi-mouse-ms-p-brain-vps35-d620n-wt-4">View</button></td>
    </tr>
    <tr id="dataset-detail-alessi-mouse-ms-p-brain-vps35-d620n-wt-4" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Brain.</h3>
          <p><strong>Dataset ID:</strong> <code>alessi-mouse-ms-p-brain-vps35-d620n-wt</code></p>
          <p><strong>Description:</strong> Proteomic characterization of brain lysosomes comparing WT and VPS35[D620N] mutant mice. Tissue was processed via glass-Teflon homogenization and 3-minute Lyso-IP. Data acquired on an Orbitrap Exploris 480 and processed using DIA-NN 1.8.1.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18476398" target="_blank" rel="noopener">10.5281/zenodo.18476398</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">alessi</span> <span class="tag-pill">brain</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, brain, alessi</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-alessi-mouse-ms-p-brain-vps35-d620n-wt</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-alessi-mouse-ms-p-brain-vps35-d620n-wt</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-alessi-mouse-ms-p-brain-vps35-d620n-wt</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-alessi-mouse-ms-p-brain-vps35-d620n-wt</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2-5" data-search="alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2 quantitative dia-based proteomic analysis of lysosomes (lyso-ip) from vps35[d620n] mouse lung with lrrk2 inhibition proteomic analysis of lung lysosomes from vps35[d620n] mice treated in vivo with mli-2 (100 mg/kg, 2 h). data acquired on an orbitrap exploris 480 and processed using dia-nn 1.8.1. na cc-by-4.0 10.5281/zenodo.18476404 alessi lung mouse mouse lung alessi gs://asap-raw-team-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2 gs://asap-dev-team-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2 gs://asap-uat-team-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2 gs://asap-curated-team-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2 v4.1.0 v4.1.0 v1.0 v4.3" data-tags="alessi||lung||mouse">
      <td><code>alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2</code></td>
      <td>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Lung with LRRK2 inhibition</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2-5">View</button></td>
    </tr>
    <tr id="dataset-detail-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2-5" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Lung with LRRK2 inhibition</h3>
          <p><strong>Dataset ID:</strong> <code>alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2</code></p>
          <p><strong>Description:</strong> Proteomic analysis of lung lysosomes from VPS35[D620N] mice treated in vivo with MLi-2 (100 mg/kg, 2 h). Data acquired on an Orbitrap Exploris 480 and processed using DIA-NN 1.8.1.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18476404" target="_blank" rel="noopener">10.5281/zenodo.18476404</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">alessi</span> <span class="tag-pill">lung</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, lung, alessi</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-alessi-mouse-ms-p-lung-vps35-d620n-dmso-mli2</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-alessi-mouse-ms-p-lung-vps35-d620n-wt-6" data-search="alessi-mouse-ms-p-lung-vps35-d620n-wt quantitative dia-based proteomic analysis of lysosomes (lyso-ip) from vps35[d620n] mouse lung basal proteomic comparison of wt and vps35[d620n] mutant lung lysosomes. data acquired on an orbitrap exploris 480 and processed using dia-nn 1.8.1. na cc-by-4.0 10.5281/zenodo.18476393 alessi lung mouse mouse lung alessi gs://asap-raw-team-alessi-mouse-ms-p-lung-vps35-d620n-wt gs://asap-dev-team-alessi-mouse-ms-p-lung-vps35-d620n-wt gs://asap-uat-team-alessi-mouse-ms-p-lung-vps35-d620n-wt gs://asap-curated-team-alessi-mouse-ms-p-lung-vps35-d620n-wt v4.1.0 v4.1.0 v1.0 v4.3" data-tags="alessi||lung||mouse">
      <td><code>alessi-mouse-ms-p-lung-vps35-d620n-wt</code></td>
      <td>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Lung</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-alessi-mouse-ms-p-lung-vps35-d620n-wt-6">View</button></td>
    </tr>
    <tr id="dataset-detail-alessi-mouse-ms-p-lung-vps35-d620n-wt-6" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Quantitative DIA-based proteomic analysis of lysosomes (Lyso-IP) from VPS35[D620N] Mouse Lung</h3>
          <p><strong>Dataset ID:</strong> <code>alessi-mouse-ms-p-lung-vps35-d620n-wt</code></p>
          <p><strong>Description:</strong> Basal proteomic comparison of WT and VPS35[D620N] mutant lung lysosomes. Data acquired on an Orbitrap Exploris 480 and processed using DIA-NN 1.8.1.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18476393" target="_blank" rel="noopener">10.5281/zenodo.18476393</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">alessi</span> <span class="tag-pill">lung</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, lung, alessi</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-alessi-mouse-ms-p-lung-vps35-d620n-wt</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-alessi-mouse-ms-p-lung-vps35-d620n-wt</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-alessi-mouse-ms-p-lung-vps35-d620n-wt</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-alessi-mouse-ms-p-lung-vps35-d620n-wt</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s-7" data-search="alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s single-nucleus transcriptomic analysis of the dorsal striatum from 6-month-old g2019s lrrk2 mutant mice we performed single-nucleus transcriptomic analysis of the dorsal striatum from 5 wild-type and 5 g2019s lrrk2 mutant mice. this dataset contains the raw fastqs files (grouped together by indexes) from mouse dorsal striatum, sorted by 10 samples (s1 to s10), with files separated by read 1 (r1), read 2 (r2), index reads (i1 and i2), and which lane they were in on the s4 flow cell (l1 to l4). these files are created by bcl2fastq of cell ranger; the sequences in those files were used for the alignments. na cc-by-4.0 10.5281/zenodo.17212215 alessi mouse-sc-rnaseq other-mouse mouse-sc-rnaseq other-mouse alessi gs://asap-raw-team-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s gs://asap-dev-team-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s gs://asap-uat-team-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s gs://asap-curated-team-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s v3.0.1 v4.0.0 v3.0.1 v1.0 v3.3 v4.0.0 v1.0 v3.3" data-tags="alessi||mouse-sc-rnaseq||other-mouse">
      <td><code>alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
      <td>Single-nucleus transcriptomic analysis of the dorsal striatum from 6-month-old G2019S LRRK2 mutant mice</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s-7">View</button></td>
    </tr>
    <tr id="dataset-detail-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s-7" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single-nucleus transcriptomic analysis of the dorsal striatum from 6-month-old G2019S LRRK2 mutant mice</h3>
          <p><strong>Dataset ID:</strong> <code>alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></p>
          <p><strong>Description:</strong> We performed single-nucleus transcriptomic analysis of the dorsal striatum from 5 wild-type and 5 G2019S LRRK2 mutant mice. This dataset contains the raw fastqs files (grouped together by indexes) from mouse dorsal striatum, sorted by 10 samples (S1 to S10), with files separated by read 1 (R1), read 2 (R2), index reads (I1 and I2), and which lane they were in on the S4 flow cell (L1 to L4). These files are created by bcl2fastq of Cell Ranger; the sequences in those files were used for the alignments.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17212215" target="_blank" rel="noopener">10.5281/zenodo.17212215</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">alessi</span> <span class="tag-pill">mouse-sc-rnaseq</span> <span class="tag-pill">other-mouse</span></p>
          <p><strong>Keywords:</strong> mouse-sc-rnaseq, other-mouse, alessi</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.1</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-alessi-mouse-sn-rnaseq-dorsal-striatum-g2019s</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-biederer-mouse-sc-rnaseq-8" data-search="biederer-mouse-sc-rnaseq singel cell rnaseq of motor cortex in a mouse model of alpha-synuclein pathology this dataset was created with the goal of identifying transcriptomic changes associated with alpha-synuclein pathology in the alpha-synuclein fibril seeding mouse model. the dataset includes single cell rna sequencing data from motor cortex of mice injected with alpha-synuclein pre-formed fibrils (“pff” group) or alpha-synuclein monomer as controls (“control” group). the dataset includes subject cohorts with different levels of the following additional experimental factors: sex (male or female); brain hemisphere relative to the pff injection site (ipsilateral or contralateral); time post-injection (1, 3, 6, or 9 months post-injection). mouse-sc-rnaseq cc-by-4.0 10.5281/zenodo.15485103 biederer mouse-other mouse-sc-rnaseq mouse-sc-rnaseq mouse-other biederer gs://asap-raw-team-biederer-mouse-sc-rnaseq gs://asap-dev-team-biederer-mouse-sc-rnaseq gs://asap-uat-team-biederer-mouse-sc-rnaseq gs://asap-curated-team-biederer-mouse-sc-rnaseq v2.0.2 v3.0.0 v4.0.0 v2.0.2 v1.0 v3.1 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3" data-tags="biederer||mouse-other||mouse-sc-rnaseq">
      <td><code>biederer-mouse-sc-rnaseq</code></td>
      <td>Singel Cell RNASeq of motor cortex in a mouse model of alpha-synuclein pathology</td>
      <td>mouse-sc-rnaseq</td>
      <td>v1.0</td>
      <td>v4.0.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-biederer-mouse-sc-rnaseq-8">View</button></td>
    </tr>
    <tr id="dataset-detail-biederer-mouse-sc-rnaseq-8" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Singel Cell RNASeq of motor cortex in a mouse model of alpha-synuclein pathology</h3>
          <p><strong>Dataset ID:</strong> <code>biederer-mouse-sc-rnaseq</code></p>
          <p><strong>Description:</strong> This dataset was created with the goal of identifying transcriptomic changes associated with alpha-synuclein pathology in the alpha-synuclein fibril seeding mouse model. The dataset includes single cell RNA Sequencing data from motor cortex of mice injected with alpha-synuclein pre-formed fibrils (“PFF” group) or alpha-synuclein monomer as controls (“Control” group). The dataset includes subject cohorts with different levels of the following additional experimental factors: sex (male or female); brain hemisphere relative to the PFF injection site (ipsilateral or contralateral); time post-injection (1, 3, 6, or 9 months post-injection).</p>
          <p><strong>Collection:</strong> mouse-sc-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15485103" target="_blank" rel="noopener">10.5281/zenodo.15485103</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">biederer</span> <span class="tag-pill">mouse-other</span> <span class="tag-pill">mouse-sc-rnaseq</span></p>
          <p><strong>Keywords:</strong> mouse-sc-rnaseq, mouse-other, biederer</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.2</td>
                <td>v1.0</td>
                <td>v3.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-biederer-mouse-sc-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-biederer-mouse-sc-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-biederer-mouse-sc-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-biederer-mouse-sc-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-cohort-mouse-sc-rnaseq-9" data-search="cohort-mouse-sc-rnaseq asap-cohort-mouse-sc-rnaseq mouse-sc-rnaseq dataset from asap-cohort mouse-sc-rnaseq cc-by-4.0 10.5281/zenodo.17860975 cohort mouse-sc-rnaseq mouse-sc-rnaseq mouse-sc-rnaseq cohort gs://asap-raw-cohort-mouse-sc-rnaseq gs://asap-dev-cohort-mouse-sc-rnaseq gs://asap-uat-cohort-mouse-sc-rnaseq gs://asap-curated-cohort-mouse-sc-rnaseq v4.0.0 v4.0.0 v1.0.0 v3.3" data-tags="cohort||mouse-sc-rnaseq">
      <td><code>cohort-mouse-sc-rnaseq</code></td>
      <td>asap-cohort-mouse-sc-rnaseq</td>
      <td>mouse-sc-rnaseq</td>
      <td>v1.0.0</td>
      <td>v4.0.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-cohort-mouse-sc-rnaseq-9">View</button></td>
    </tr>
    <tr id="dataset-detail-cohort-mouse-sc-rnaseq-9" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>asap-cohort-mouse-sc-rnaseq</h3>
          <p><strong>Dataset ID:</strong> <code>cohort-mouse-sc-rnaseq</code></p>
          <p><strong>Description:</strong> mouse-sc-rnaseq dataset from asap-cohort</p>
          <p><strong>Collection:</strong> mouse-sc-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.0.0</p>
          <p><strong>Latest release:</strong> v4.0.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17860975" target="_blank" rel="noopener">10.5281/zenodo.17860975</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">cohort</span> <span class="tag-pill">mouse-sc-rnaseq</span></p>
          <p><strong>Keywords:</strong> mouse-sc-rnaseq, mouse-sc-rnaseq, cohort</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0.0</td>
                <td>v3.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-cohort-mouse-sc-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-cohort-mouse-sc-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-cohort-mouse-sc-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-cohort-mouse-sc-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-cohort-pmdbs-bulk-rnaseq-10" data-search="cohort-pmdbs-bulk-rnaseq asap-cohort-pmdbs-bulk-rnaseq pmdbs-bulk-rnaseq dataset from asap-cohort pmdbs-bulk-rnaseq cc-by-4.0 10.5281/zenodo.16975686 cohort pmdbs-bulk-rnaseq pmdbs-bulk-rnaseq pmdbs-bulk-rnaseq cohort gs://asap-raw-cohort-pmdbs-bulk-rnaseq gs://asap-dev-cohort-pmdbs-bulk-rnaseq gs://asap-uat-cohort-pmdbs-bulk-rnaseq gs://asap-curated-cohort-pmdbs-bulk-rnaseq v2.0.0 v3.0.0 v4.0.0 v4.1.0 v2.0.0 v1.0.0 v3.0 v3.0.0 v1.1.0 v3.2 v4.0.0 v1.2.0 v3.3 v4.1.0 v1.2.1 v3.3" data-tags="cohort||pmdbs-bulk-rnaseq">
      <td><code>cohort-pmdbs-bulk-rnaseq</code></td>
      <td>asap-cohort-pmdbs-bulk-rnaseq</td>
      <td>pmdbs-bulk-rnaseq</td>
      <td>v1.2.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-cohort-pmdbs-bulk-rnaseq-10">View</button></td>
    </tr>
    <tr id="dataset-detail-cohort-pmdbs-bulk-rnaseq-10" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>asap-cohort-pmdbs-bulk-rnaseq</h3>
          <p><strong>Dataset ID:</strong> <code>cohort-pmdbs-bulk-rnaseq</code></p>
          <p><strong>Description:</strong> pmdbs-bulk-rnaseq dataset from asap-cohort</p>
          <p><strong>Collection:</strong> pmdbs-bulk-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.2.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16975686" target="_blank" rel="noopener">10.5281/zenodo.16975686</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">cohort</span> <span class="tag-pill">pmdbs-bulk-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs-bulk-rnaseq, pmdbs-bulk-rnaseq, cohort</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.2.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.2.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v1.0.0</td>
                <td>v3.0</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-cohort-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-cohort-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-cohort-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-cohort-pmdbs-bulk-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-cohort-pmdbs-sc-rnaseq-11" data-search="cohort-pmdbs-sc-rnaseq asap-cohort-pmdbs-sc-rnaseq pmdbs-sc-rnaseq dataset from asap-cohort pmdbs-sc-rnaseq cc-by-4.0 10.5281/zenodo.19876217 cohort pmdbs-sc-rnaseq pmdbs-sc-rnaseq pmdbs-sc-rnaseq cohort gs://asap-raw-cohort-pmdbs-sc-rnaseq gs://asap-dev-cohort-pmdbs-sc-rnaseq gs://asap-uat-cohort-pmdbs-sc-rnaseq gs://asap-curated-cohort-pmdbs-sc-rnaseq v1.0.0 v2.0.0 v3.0.0 v4.0.0 v4.1.0 v1.0.0 v1.0.0 v2.1 v2.0.0 v2.0.0 v3.0 v3.0.0 v3.0.0 v3.2 v4.0.0 v3.1.0 v3.3 v4.1.0 v3.1.1 v3.3" data-tags="cohort||pmdbs-sc-rnaseq">
      <td><code>cohort-pmdbs-sc-rnaseq</code></td>
      <td>asap-cohort-pmdbs-sc-rnaseq</td>
      <td>pmdbs-sc-rnaseq</td>
      <td>v3.1.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-cohort-pmdbs-sc-rnaseq-11">View</button></td>
    </tr>
    <tr id="dataset-detail-cohort-pmdbs-sc-rnaseq-11" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>asap-cohort-pmdbs-sc-rnaseq</h3>
          <p><strong>Dataset ID:</strong> <code>cohort-pmdbs-sc-rnaseq</code></p>
          <p><strong>Description:</strong> pmdbs-sc-rnaseq dataset from asap-cohort</p>
          <p><strong>Collection:</strong> pmdbs-sc-rnaseq</p>
          <p><strong>Current dataset version:</strong> v3.1.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.19876217" target="_blank" rel="noopener">10.5281/zenodo.19876217</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">cohort</span> <span class="tag-pill">pmdbs-sc-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs-sc-rnaseq, pmdbs-sc-rnaseq, cohort</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v3.1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v3.1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v3.0.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v2.0.0</td>
                <td>v3.0</td>
              </tr>
              <tr>
                <td>v1.0.0</td>
                <td>v1.0.0</td>
                <td>v2.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-cohort-pmdbs-sc-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-cohort-pmdbs-sc-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-cohort-pmdbs-sc-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-cohort-pmdbs-sc-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-cragg-mouse-sn-rnaseq-striatum-12" data-search="cragg-mouse-sn-rnaseq-striatum single nucleus rna sequencing of the striatum of two murine parkinson&#x27;s disease models. this dataset includes single-nucleus rna sequencing (snrna-seq) data derived from mouse models of parkinson&#x27;s disease (pd), designed to capture both cell-type-specific and spatial gene expression changes across different stages and mechanisms of pd-like pathology.  single-nucleus rna sequencing (snrna-seq) was performed on mouse striatal tissue from two distinct pd models: 

1. mild neurotoxin model (6-ohda): adult wild-type mice received unilateral injections of 6-hydroxydopamine (6-ohda) at a low dose (0.6 µg/µl) into the medial forebrain bundle (mfb), selectively damaging nigrostriatal dopaminergic neurons and inducing mild parkinsonian pathology. untreated wild-type mice served as controls. 

2. progressive genetic model (mitopark): the mitopark model (slc6a3-cre; tfam^flx/flx) induces mitochondrial dysfunction specifically in dopaminergic neurons, leading to progressive neurodegeneration. samples were collected at two timepoints: 
	* 10–11 weeks of age: early stage, pre-symptomatic or mildly affected, and  
	* 15–18 weeks of age: late stage, with clear motor deficits and advanced degeneration.   this snrna-seq dataset enables in-depth analysis of transcriptomic alterations across distinct pd etiologies and stages. mouse-sc-rnaseq cc-by-4.0 10.5281/zenodo.15400039 cragg mouse-other mouse-sc-rnaseq mouse-sc-rnaseq mouse-other cragg gs://asap-raw-team-cragg-mouse-sn-rnaseq-striatum gs://asap-dev-team-cragg-mouse-sn-rnaseq-striatum gs://asap-uat-team-cragg-mouse-sn-rnaseq-striatum gs://asap-curated-team-cragg-mouse-sn-rnaseq-striatum v2.0.2 v3.0.0 v4.0.0 v2.0.2 v1.0 v3.1 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3" data-tags="cragg||mouse-other||mouse-sc-rnaseq">
      <td><code>cragg-mouse-sn-rnaseq-striatum</code></td>
      <td>Single Nucleus RNA sequencing of the Striatum of Two Murine Parkinson&#x27;s Disease Models.</td>
      <td>mouse-sc-rnaseq</td>
      <td>v1.0</td>
      <td>v4.0.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-cragg-mouse-sn-rnaseq-striatum-12">View</button></td>
    </tr>
    <tr id="dataset-detail-cragg-mouse-sn-rnaseq-striatum-12" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single Nucleus RNA sequencing of the Striatum of Two Murine Parkinson&#x27;s Disease Models.</h3>
          <p><strong>Dataset ID:</strong> <code>cragg-mouse-sn-rnaseq-striatum</code></p>
          <p><strong>Description:</strong> This dataset includes single-nucleus RNA sequencing (snRNA-seq) data derived from mouse models of Parkinson&#x27;s disease (PD), designed to capture both cell-type-specific and spatial gene expression changes across different stages and mechanisms of PD-like pathology.  Single-nucleus RNA sequencing (snRNA-seq) was performed on mouse striatal tissue from two distinct PD models: 

1. Mild Neurotoxin Model (6-OHDA): Adult wild-type mice received unilateral injections of 6-hydroxydopamine (6-OHDA) at a low dose (0.6 µg/µL) into the medial forebrain bundle (MFB), selectively damaging nigrostriatal dopaminergic neurons and inducing mild Parkinsonian pathology. Untreated wild-type mice served as controls. 

2. Progressive Genetic Model (MitoPark): The MitoPark model (Slc6a3-cre; Tfam^flx/flx) induces mitochondrial dysfunction specifically in dopaminergic neurons, leading to progressive neurodegeneration. Samples were collected at two timepoints: 
	* 10–11 weeks of age: Early stage, pre-symptomatic or mildly affected, and  
	* 15–18 weeks of age: Late stage, with clear motor deficits and advanced degeneration.   This snRNA-seq dataset enables in-depth analysis of transcriptomic alterations across distinct PD etiologies and stages.</p>
          <p><strong>Collection:</strong> mouse-sc-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15400039" target="_blank" rel="noopener">10.5281/zenodo.15400039</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">cragg</span> <span class="tag-pill">mouse-other</span> <span class="tag-pill">mouse-sc-rnaseq</span></p>
          <p><strong>Keywords:</strong> mouse-sc-rnaseq, mouse-other, cragg</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.2</td>
                <td>v1.0</td>
                <td>v3.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-cragg-mouse-sn-rnaseq-striatum</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-cragg-mouse-sn-rnaseq-striatum</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-cragg-mouse-sn-rnaseq-striatum</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-cragg-mouse-sn-rnaseq-striatum</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-cragg-mouse-spatial-visium-striatum-13" data-search="cragg-mouse-spatial-visium-striatum spatial transcriptomics of the striatum of two murine parkinson&#x27;s disease models. this dataset includes spatial transcriptomics (st) data derived from mouse models of parkinson’s disease (pd), designed to capture both cell-type-specific and spatial gene expression changes across different stages and mechanisms of pd-like pathology. the mild neurotoxin model (6-ohda): adult wild-type mice received unilateral injections of 6-hydroxydopamine (6-ohda) at a low dose (0.6 µg/µl) into the medial forebrain bundle (mfb), selectively damaging nigrostriatal dopaminergic neurons and inducing mild parkinsonian pathology. untreated wild-type mice served as controls. spatial gene expression profiling was conducted on the striata of mice from the mild 6-ohda model to preserve anatomical context. tissue sections were collected from six adult mice — three 6-ohda-treated and three untreated controls. for each animal, four rostro-caudal levels of the striatum were analyzed, capturing regional heterogeneity in response to dopaminergic denervation. the 10x genomics visium platform was used to generate spatially resolved transcriptomic maps. this st dataset allows for the visualization and quantification of spatial patterns in gene expression following mild dopaminergic injury, complementing the cell-type-specific insights gained from the snrna-seq data. mouse-spatial-rnaseq cc-by-4.0 10.5281/zenodo.15428115 cragg mouse-other mouse-spatial-rnaseq mouse-spatial-rnaseq mouse-other cragg gs://asap-raw-team-cragg-mouse-spatial-visium-striatum gs://asap-dev-team-cragg-mouse-spatial-visium-striatum gs://asap-uat-team-cragg-mouse-spatial-visium-striatum gs://asap-curated-team-cragg-mouse-spatial-visium-striatum v2.0.3 v3.0.0 v4.0.0 v2.0.3 v1.0 v3.1 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3" data-tags="cragg||mouse-other||mouse-spatial-rnaseq">
      <td><code>cragg-mouse-spatial-visium-striatum</code></td>
      <td>Spatial Transcriptomics of the Striatum of Two Murine Parkinson&#x27;s Disease Models.</td>
      <td>mouse-spatial-rnaseq</td>
      <td>v1.0</td>
      <td>v4.0.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-cragg-mouse-spatial-visium-striatum-13">View</button></td>
    </tr>
    <tr id="dataset-detail-cragg-mouse-spatial-visium-striatum-13" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Spatial Transcriptomics of the Striatum of Two Murine Parkinson&#x27;s Disease Models.</h3>
          <p><strong>Dataset ID:</strong> <code>cragg-mouse-spatial-visium-striatum</code></p>
          <p><strong>Description:</strong> This dataset includes Spatial Transcriptomics (ST) data derived from mouse models of Parkinson’s disease (PD), designed to capture both cell-type-specific and spatial gene expression changes across different stages and mechanisms of PD-like pathology. The Mild Neurotoxin Model (6-OHDA): Adult wild-type mice received unilateral injections of 6-hydroxydopamine (6-OHDA) at a low dose (0.6 µg/µL) into the medial forebrain bundle (MFB), selectively damaging nigrostriatal dopaminergic neurons and inducing mild Parkinsonian pathology. Untreated wild-type mice served as controls. Spatial gene expression profiling was conducted on the striata of mice from the mild 6-OHDA model to preserve anatomical context. Tissue sections were collected from six adult mice — three 6-OHDA-treated and three untreated controls. For each animal, four rostro-caudal levels of the striatum were analyzed, capturing regional heterogeneity in response to dopaminergic denervation. The 10X Genomics Visium platform was used to generate spatially resolved transcriptomic maps. This ST dataset allows for the visualization and quantification of spatial patterns in gene expression following mild dopaminergic injury, complementing the cell-type-specific insights gained from the snRNA-seq data.</p>
          <p><strong>Collection:</strong> mouse-spatial-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15428115" target="_blank" rel="noopener">10.5281/zenodo.15428115</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">cragg</span> <span class="tag-pill">mouse-other</span> <span class="tag-pill">mouse-spatial-rnaseq</span></p>
          <p><strong>Keywords:</strong> mouse-spatial-rnaseq, mouse-other, cragg</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.3</td>
                <td>v1.0</td>
                <td>v3.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-cragg-mouse-spatial-visium-striatum</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-cragg-mouse-spatial-visium-striatum</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-cragg-mouse-spatial-visium-striatum</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-cragg-mouse-spatial-visium-striatum</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-edwards-pmdbs-spatial-geomx-th-14" data-search="edwards-pmdbs-spatial-geomx-th spatial transcriptomics data (geomx) of midbrain dopamine cells in control and pd subjects the repository includes spatial transcriptomic datasets generated by nanostring geomx (hu wta) analysis of midbrain th+ cells from controls (n=10), incidental lewy body disease (n=10), early parkinsons disease (epd,n=5) and late parkinsons disease (lpd,n=5). a total 348 regions of interest were analysed. the raw and processed counts and metadata are provided as an r seurat object (geomx_edwards_thmask.rds). the scripts used for low level data processing are described in https://github.com/zchatt/asap-spatialtranscriptomics/blob/main/geomx/lowlevel/readme.md  tissue samples from pathologically confirmed asymptomatic stage i-ii lewy body disease, stage iv lewy body pd (early-pd), stage vi lewy body pd (late-pd)(braak, del tredici et al. 2003) and controls without the neurological or neuropathological disease were obtained from the sydney brain bank. the study was approved by the university of sydney human research ethics committee (2021/845). all cases with pd were levodopa-responsive and fulfilled the uk brain bank clinical criteria for a diagnosis of clinical pd (hughes, ben-shlomo et al. 1992) with no other neurodegenerative conditions.   cells were not extracted. tissue sections were cut from ffpe blocks of post-mortem human midbrains at 6µm on a rotary microtome (histocore multicut, leica biosystems) and mounted on series 2 adhesive microscope slides (trajan scientific medical, au) for processing for spatial trranscriptomics. to remove the paraffin, slides were incubated in the oven at 60°c for 1hr and then submerged in histochoice clearing agent (sigma-aldrich, h2779) for 2x7mins, followed by rehydration in decreasing ethanol concentrations (100% ethanol for 2x3mins, 95% ethanol for 3mins, 70% ethanol for 3mins) and distilled h2o for 3mins.   tissue sections were immunohistochemically stained for tyrosine hydroxylase and regions of interest (rois) processed following nanostring geomx® digital spatial profiler using the manufacturer’s instructions. libraries were sequenced on illumina novaseq 6000 platform using novaseq sp 100 cycle kit (xp workflow, 27-8-8-27).  this research was funded in whole or in part by aligning science across parkinson’s (asap-020529) through the michael j. fox foundation for parkinson’s research (mjff). for the purpose of open access, the author has applied a cc by 4.0 public copyright license to all author accepted manuscripts arising from this submission. pmdbs-spatial-rnaseq cc-by-4.0 10.5281/zenodo.15480990 edwards pmdbs-other pmdbs-spatial-rnaseq pmdbs-spatial-rnaseq pmdbs-other edwards gs://asap-raw-team-edwards-pmdbs-spatial-geomx-th gs://asap-dev-team-edwards-pmdbs-spatial-geomx-th gs://asap-uat-team-edwards-pmdbs-spatial-geomx-th gs://asap-curated-team-edwards-pmdbs-spatial-geomx-th v2.0.2 v3.0.0 v4.0.0 v2.0.2 v1.0 v3.1 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3" data-tags="edwards||pmdbs-other||pmdbs-spatial-rnaseq">
      <td><code>edwards-pmdbs-spatial-geomx-th</code></td>
      <td>Spatial Transcriptomics data (GeoMx) of midbrain dopamine cells in control and PD subjects</td>
      <td>pmdbs-spatial-rnaseq</td>
      <td>v1.0</td>
      <td>v4.0.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-edwards-pmdbs-spatial-geomx-th-14">View</button></td>
    </tr>
    <tr id="dataset-detail-edwards-pmdbs-spatial-geomx-th-14" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Spatial Transcriptomics data (GeoMx) of midbrain dopamine cells in control and PD subjects</h3>
          <p><strong>Dataset ID:</strong> <code>edwards-pmdbs-spatial-geomx-th</code></p>
          <p><strong>Description:</strong> The repository includes Spatial Transcriptomic datasets generated by Nanostring GeoMx (Hu WTA) analysis of midbrain TH+ cells from Controls (n=10), Incidental Lewy Body Disease (n=10), early Parkinsons Disease (ePD,n=5) and late Parkinsons Disease (lPD,n=5). A total 348 Regions of Interest were analysed. The raw and processed counts and metadata are provided as an R Seurat object (geomx_edwards_thmask.rds). The scripts used for low level data processing are described in https://github.com/zchatt/ASAP-SpatialTranscriptomics/blob/main/geomx/lowlevel/README.md  Tissue samples from pathologically confirmed asymptomatic stage I-II Lewy body disease, stage IV Lewy body PD (early-PD), stage VI Lewy body PD (late-PD)(Braak, Del Tredici et al. 2003) and controls without the neurological or neuropathological disease were obtained from the Sydney Brain Bank. The study was approved by the University of Sydney Human Research Ethics Committee (2021/845). All cases with PD were levodopa-responsive and fulfilled the UK Brain Bank Clinical Criteria for a diagnosis of clinical PD (Hughes, Ben-Shlomo et al. 1992) with no other neurodegenerative conditions.   Cells were not extracted. Tissue sections were cut from FFPE blocks of post-mortem human midbrains at 6µm on a rotary microtome (HistoCore MULTICUT, Leica Biosystems) and mounted on Series 2 adhesive microscope slides (Trajan Scientific Medical, AU) for processing for spatial trranscriptomics. To remove the paraffin, slides were incubated in the oven at 60°C for 1hr and then submerged in HistoChoice Clearing Agent (Sigma-Aldrich, H2779) for 2x7mins, followed by rehydration in decreasing ethanol concentrations (100% ethanol for 2x3mins, 95% ethanol for 3mins, 70% ethanol for 3mins) and distilled H2O for 3mins.   Tissue sections were immunohistochemically stained for tyrosine hydroxylase and Regions of Interest (ROIs) processed following Nanostring GeoMx® Digital Spatial Profiler using the manufacturer’s instructions. Libraries were sequenced on Illumina Novaseq 6000 platform using NovaSeq SP 100 cycle kit (XP workflow, 27-8-8-27).  This research was funded in whole or in part by Aligning Science Across Parkinson’s (ASAP-020529) through the Michael J. Fox Foundation for Parkinson’s Research (MJFF). For the purpose of open access, the author has applied a CC BY 4.0 public copyright license to all Author Accepted Manuscripts arising from this submission.</p>
          <p><strong>Collection:</strong> pmdbs-spatial-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15480990" target="_blank" rel="noopener">10.5281/zenodo.15480990</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">edwards</span> <span class="tag-pill">pmdbs-other</span> <span class="tag-pill">pmdbs-spatial-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs-spatial-rnaseq, pmdbs-other, edwards</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.2</td>
                <td>v1.0</td>
                <td>v3.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-edwards-pmdbs-spatial-geomx-th</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-edwards-pmdbs-spatial-geomx-th</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-edwards-pmdbs-spatial-geomx-th</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-edwards-pmdbs-spatial-geomx-th</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-hafler-pmdbs-sn-rnaseq-pfc-15" data-search="hafler-pmdbs-sn-rnaseq-pfc single-cell transcriptomic and proteomic analysis of parkinson’s disease brains to identify and characterize selectively vulnerable brain cell populations in parkinson’s disease (pd), we performed single nucleus transcriptomics and unbiased proteomics to profile the prefrontal cortex from postmortem human brains of six individuals with late-stage pd and six age-matched controls. analysis of nearly 80,000 nuclei led to the identification of eight major brain cell types, including elevated brain-resident t cells in pd, each with distinct transcriptional changes in agreement with the known genetics of pd. by analyzing lewy body pathology in the same postmortem brain tissues, we found that α-synuclein pathology was inversely correlated with chaperone expression in excitatory neurons. examining cell-cell interactions, we found a selective abatement of neuron-astrocyte interactions and enhanced neuroinflammation. proteomic analyses of the same brains identified synaptic proteins in the prefrontal cortex that were preferentially downregulated in pd. by comparing this single cell pd dataset with a published analysis of similar brain regions in alzheimer’s disease (ad), we found no common differentially expressed genes in neurons but identified many shared differentially expressed genes in glial cells, suggesting that the disease etiologies, especially in the context of neuronal vulnerability, in pd and ad are likely distinct. to prepare these samples, nuclei were isolated from post-mortem, fresh-frozen human brain tissue. approximately 50 to 100 mg of frozen tissue was homogenized in 15 ml of ice-cold nuclei homogenization buffer [2 m sucrose, 10 mm hepes (ph 7.9), 25 mm kcl, 1 mm edta (ph 8.0), 10% glycerol, with freshly added rnase inhibitors (80 u/ml)] using a dounce tissue grinder (10 strokes with the loose pestle, followed by 10 strokes with the tight pestle). the homogenate was layered over 10 ml of fresh homogenization buffer in an ultracentrifuge tube and centrifuged at 25,000 rpm for 60 minutes at 4°c. after ultracentrifugation, the supernatant was discarded, and the nuclei pellet was resuspended in 1 ml of nuclei resuspension buffer [15 mm hepes (ph 7.4), 15 mm nacl, 60 mm kcl, 2 mm mgcl₂, 3 mm cacl₂, with freshly added rnase inhibitors (80 u/ml)] and counted using a hemocytometer prior to loading for 10x genomics platform.  the snrna-seq libraries were prepared by the 10x genomics chromium single cell 3&#x27; reagent kit v3 chemistry according to the manufacturer&#x27;s instructions and sequenced using illumina novaseq6000 s4 sequencer. a custom pre-mrna human genome reference was generated with grch38 (ensembl 93) that included pre-mrna sequences by 10x cell ranger. snrna-seq data were aligned to this grch38 pre-mrna human genome reference (ensembl 93) to map both unspliced pre-mrna and mature mrna using 10x cellranger version 3.1.0. pmdbs-sc-rnaseq cc-by-4.0 10.5281/zenodo.15490150 hafler pmdbs-sc-rnaseq pmdbs-sc-rnaseq pmdbs-sc-rnaseq hafler gs://asap-raw-team-hafler-pmdbs-sn-rnaseq-pfc gs://asap-dev-team-hafler-pmdbs-sn-rnaseq-pfc gs://asap-uat-team-hafler-pmdbs-sn-rnaseq-pfc gs://asap-curated-team-hafler-pmdbs-sn-rnaseq-pfc v1.0.0 v2.0.0 v3.0.0 v4.0.0 v4.1.0 v1.0.0 v1.0 v2.1 v2.0.0 v1.0 v3.0 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3 v4.1.0 v1.1 v3.3" data-tags="hafler||pmdbs-sc-rnaseq">
      <td><code>hafler-pmdbs-sn-rnaseq-pfc</code></td>
      <td>Single-cell transcriptomic and proteomic analysis of Parkinson’s disease brains</td>
      <td>pmdbs-sc-rnaseq</td>
      <td>v1.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-hafler-pmdbs-sn-rnaseq-pfc-15">View</button></td>
    </tr>
    <tr id="dataset-detail-hafler-pmdbs-sn-rnaseq-pfc-15" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single-cell transcriptomic and proteomic analysis of Parkinson’s disease brains</h3>
          <p><strong>Dataset ID:</strong> <code>hafler-pmdbs-sn-rnaseq-pfc</code></p>
          <p><strong>Description:</strong> To identify and characterize selectively vulnerable brain cell populations in Parkinson’s disease (PD), we performed single nucleus transcriptomics and unbiased proteomics to profile the prefrontal cortex from postmortem human brains of six individuals with late-stage PD and six age-matched controls. Analysis of nearly 80,000 nuclei led to the identification of eight major brain cell types, including elevated brain-resident T cells in PD, each with distinct transcriptional changes in agreement with the known genetics of PD. By analyzing Lewy body pathology in the same postmortem brain tissues, we found that α-synuclein pathology was inversely correlated with chaperone expression in excitatory neurons. Examining cell-cell interactions, we found a selective abatement of neuron-astrocyte interactions and enhanced neuroinflammation. Proteomic analyses of the same brains identified synaptic proteins in the prefrontal cortex that were preferentially downregulated in PD. By comparing this single cell PD dataset with a published analysis of similar brain regions in Alzheimer’s disease (AD), we found no common differentially expressed genes in neurons but identified many shared differentially expressed genes in glial cells, suggesting that the disease etiologies, especially in the context of neuronal vulnerability, in PD and AD are likely distinct. To prepare these samples, nuclei were isolated from post-mortem, fresh-frozen human brain tissue. Approximately 50 to 100 mg of frozen tissue was homogenized in 15 ml of ice-cold nuclei homogenization buffer [2 M sucrose, 10 mM HEPES (pH 7.9), 25 mM KCl, 1 mM EDTA (pH 8.0), 10% glycerol, with freshly added RNase inhibitors (80 U/ml)] using a Dounce tissue grinder (10 strokes with the loose pestle, followed by 10 strokes with the tight pestle). The homogenate was layered over 10 ml of fresh homogenization buffer in an ultracentrifuge tube and centrifuged at 25,000 rpm for 60 minutes at 4°C. After ultracentrifugation, the supernatant was discarded, and the nuclei pellet was resuspended in 1 ml of nuclei resuspension buffer [15 mM HEPES (pH 7.4), 15 mM NaCl, 60 mM KCl, 2 mM MgCl₂, 3 mM CaCl₂, with freshly added RNase inhibitors (80 U/ml)] and counted using a hemocytometer prior to loading for 10x Genomics platform.  The snRNA-seq libraries were prepared by the 10x Genomics Chromium Single Cell 3&#x27; Reagent Kit v3 chemistry according to the manufacturer&#x27;s instructions and sequenced using Illumina NovaSeq6000 S4 sequencer. A custom pre-mRNA human genome reference was generated with GRCh38 (Ensembl 93) that included pre-mRNA sequences by 10x Cell Ranger. snRNA-seq data were aligned to this GRCh38 pre-mRNA human genome reference (Ensembl 93) to map both unspliced pre-mRNA and mature mRNA using 10x CellRanger version 3.1.0.</p>
          <p><strong>Collection:</strong> pmdbs-sc-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15490150" target="_blank" rel="noopener">10.5281/zenodo.15490150</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">hafler</span> <span class="tag-pill">pmdbs-sc-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs-sc-rnaseq, pmdbs-sc-rnaseq, hafler</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v1.0</td>
                <td>v3.0</td>
              </tr>
              <tr>
                <td>v1.0.0</td>
                <td>v1.0</td>
                <td>v2.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-hafler-pmdbs-sn-rnaseq-pfc</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-hafler-pmdbs-sn-rnaseq-pfc</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-hafler-pmdbs-sn-rnaseq-pfc</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-hafler-pmdbs-sn-rnaseq-pfc</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-hardy-pmdbs-bulk-rnaseq-16" data-search="hardy-pmdbs-bulk-rnaseq bulk rna sequencing of human post-mortem brain tissue from parkinson&#x27;s disease and control donors bulk rna-seq data from 288 samples derived from pmdbs samples across anterior cingulate cortex (acg), inferior parietal lobule (ipl), middle frontal gyrus (mfg), and middle temporal gyrus (mtg) types of samples: late stage (braak 6) pd and control post-mortem brains. pmdbs-bulk-rnaseq cc-by-4.0 10.5281/zenodo.16749098 hardy pmdbs-bulk-rnaseq pmdbs-bulk-rnaseq pmdbs-bulk-rnaseq hardy gs://asap-raw-team-hardy-pmdbs-bulk-rnaseq gs://asap-dev-team-hardy-pmdbs-bulk-rnaseq gs://asap-uat-team-hardy-pmdbs-bulk-rnaseq gs://asap-curated-team-hardy-pmdbs-bulk-rnaseq v2.0.0 v3.0.0 v4.0.0 v4.1.0 v2.0.0 v1.0 v3.0 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3 v4.1.0 v1.1 v3.3" data-tags="hardy||pmdbs-bulk-rnaseq">
      <td><code>hardy-pmdbs-bulk-rnaseq</code></td>
      <td>Bulk RNA sequencing of human post-mortem brain tissue from Parkinson&#x27;s disease and control donors</td>
      <td>pmdbs-bulk-rnaseq</td>
      <td>v1.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-hardy-pmdbs-bulk-rnaseq-16">View</button></td>
    </tr>
    <tr id="dataset-detail-hardy-pmdbs-bulk-rnaseq-16" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Bulk RNA sequencing of human post-mortem brain tissue from Parkinson&#x27;s disease and control donors</h3>
          <p><strong>Dataset ID:</strong> <code>hardy-pmdbs-bulk-rnaseq</code></p>
          <p><strong>Description:</strong> Bulk RNA-seq data from 288 samples derived from PMDBS samples across Anterior Cingulate Cortex (ACG), Inferior Parietal Lobule (IPL), Middle Frontal Gyrus (MFG), and Middle Temporal Gyrus (MTG) Types of Samples: Late stage (Braak 6) PD and control post-mortem brains.</p>
          <p><strong>Collection:</strong> pmdbs-bulk-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16749098" target="_blank" rel="noopener">10.5281/zenodo.16749098</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">hardy</span> <span class="tag-pill">pmdbs-bulk-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs-bulk-rnaseq, pmdbs-bulk-rnaseq, hardy</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v1.0</td>
                <td>v3.0</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-hardy-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-hardy-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-hardy-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-hardy-pmdbs-bulk-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-hardy-pmdbs-sn-rnaseq-17" data-search="hardy-pmdbs-sn-rnaseq single-nucleus rna sequencing of human post-mortem brain tissue from parkinson&#x27;s disease and control donors bulk rna-seq data from 128 samples derived from pmdbs samples across inferior parietal lobule (ipl), and anterior cingulate cortex (acg). types of samples: late stage (braak 5-6) pd and control post-mortem brains. pmdbs-sc-rnaseq cc-by-4.0 10.5281/zenodo.16749080 hardy pmdbs-sc-rnaseq pmdbs-sc-rnaseq pmdbs-sc-rnaseq hardy gs://asap-raw-team-hardy-pmdbs-sn-rnaseq gs://asap-dev-team-hardy-pmdbs-sn-rnaseq gs://asap-uat-team-hardy-pmdbs-sn-rnaseq gs://asap-curated-team-hardy-pmdbs-sn-rnaseq v2.0.0 v3.0.0 v4.0.0 v4.1.0 v2.0.0 v1.0 v3.0 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3 v4.1.0 v1.1 v3.3" data-tags="hardy||pmdbs-sc-rnaseq">
      <td><code>hardy-pmdbs-sn-rnaseq</code></td>
      <td>Single-nucleus RNA sequencing of human post-mortem brain tissue from Parkinson&#x27;s disease and control donors</td>
      <td>pmdbs-sc-rnaseq</td>
      <td>v1.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-hardy-pmdbs-sn-rnaseq-17">View</button></td>
    </tr>
    <tr id="dataset-detail-hardy-pmdbs-sn-rnaseq-17" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single-nucleus RNA sequencing of human post-mortem brain tissue from Parkinson&#x27;s disease and control donors</h3>
          <p><strong>Dataset ID:</strong> <code>hardy-pmdbs-sn-rnaseq</code></p>
          <p><strong>Description:</strong> Bulk RNA-seq data from 128 samples derived from PMDBS samples across Inferior Parietal Lobule (IPL), and Anterior Cingulate Cortex (ACG). Types of Samples: Late stage (Braak 5-6) PD and control post-mortem brains.</p>
          <p><strong>Collection:</strong> pmdbs-sc-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16749080" target="_blank" rel="noopener">10.5281/zenodo.16749080</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">hardy</span> <span class="tag-pill">pmdbs-sc-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs-sc-rnaseq, pmdbs-sc-rnaseq, hardy</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v1.0</td>
                <td>v3.0</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-hardy-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-hardy-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-hardy-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-hardy-pmdbs-sn-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-jakobsson-invitro-bulk-rnaseq-dopaminergic-18" data-search="jakobsson-invitro-bulk-rnaseq-dopaminergic bulk rnaseq of dopaminergic neurons in vitro cultures this dataset includes bulk rnaseq (2 x 150bps reads; illumina truseq stranded mrna library prep kit with poly-a selection) of differentiated human embryonic stem cells into dopaminergic neurons. briefly, hes (rc17) and hipscs (kolf2.1) were differentiated towards ventral midbrain (vmb) fate based on a previously published protocol (nolbrant et al, 2017). detailed protocols for generation of human ventral midbrain dopaminergic progenitors and dopaminergic neurons can be found at dx.doi.org/10.17504/protocols.io.kxygx4eqol8j/v1 and dx.doi.org/10.17504/protocols.io.q26g7nbd1lwz/v1, respectively. na cc-by-4.0 10.5281/zenodo.17149266 invitro invitro-bulk-rnaseq jakobsson invitro-bulk-rnaseq invitro jakobsson gs://asap-raw-team-jakobsson-invitro-bulk-rnaseq-dopaminergic gs://asap-dev-team-jakobsson-invitro-bulk-rnaseq-dopaminergic gs://asap-uat-team-jakobsson-invitro-bulk-rnaseq-dopaminergic gs://asap-curated-team-jakobsson-invitro-bulk-rnaseq-dopaminergic v3.0.2 v4.0.0 v3.0.2 v1.0 v3.3 v4.0.0 v1.0 v3.3" data-tags="invitro||invitro-bulk-rnaseq||jakobsson">
      <td><code>jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
      <td>Bulk RNAseq of dopaminergic neurons in vitro cultures</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-jakobsson-invitro-bulk-rnaseq-dopaminergic-18">View</button></td>
    </tr>
    <tr id="dataset-detail-jakobsson-invitro-bulk-rnaseq-dopaminergic-18" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Bulk RNAseq of dopaminergic neurons in vitro cultures</h3>
          <p><strong>Dataset ID:</strong> <code>jakobsson-invitro-bulk-rnaseq-dopaminergic</code></p>
          <p><strong>Description:</strong> This dataset includes bulk RNAseq (2 x 150bps reads; Illumina TruSeq Stranded mRNA library prep kit with poly-A selection) of differentiated human embryonic stem cells into dopaminergic neurons. Briefly, hES (RC17) and hiPSCs (KOLF2.1) were differentiated towards ventral midbrain (vMB) fate based on a previously published protocol (Nolbrant et al, 2017). Detailed protocols for generation of human ventral midbrain dopaminergic progenitors and dopaminergic neurons can be found at dx.doi.org/10.17504/protocols.io.kxygx4eqol8j/v1 and dx.doi.org/10.17504/protocols.io.q26g7nbd1lwz/v1, respectively.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17149266" target="_blank" rel="noopener">10.5281/zenodo.17149266</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">invitro</span> <span class="tag-pill">invitro-bulk-rnaseq</span> <span class="tag-pill">jakobsson</span></p>
          <p><strong>Keywords:</strong> invitro-bulk-rnaseq, invitro, jakobsson</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.2</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-jakobsson-invitro-bulk-rnaseq-dopaminergic</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-jakobsson-invitro-bulk-rnaseq-microglia-19" data-search="jakobsson-invitro-bulk-rnaseq-microglia bulk rnaseq of microglia in vitro cultures this dataset includes bulk rnaseq (2 x 150bps reads; illumina truseq stranded mrna library prep kit with poly-a selection) of differentiated human pluripotent stem cells (hpscs) into microglia. briefly, hes (h9) and hipscs (kolf2.1) underwent mesodermal induction via embryoid body formation, followed by hemogenic endothelium induction and myeloid differentiation to generate primitive monocyte-like precursors. these precursors were then matured into microglia by supplementing with key neuron-derived factors that promote microglial identity, thereby recapitulating human microglia in monoculture. a detailed protocol can be found at doi: dx.doi.org/10.17504/protocols.io.14egnr8ezl5d/v1. na cc-by-4.0 10.5281/zenodo.17149290 invitro invitro-bulk-rnaseq jakobsson invitro-bulk-rnaseq invitro jakobsson gs://asap-raw-team-jakobsson-invitro-bulk-rnaseq-microglia gs://asap-dev-team-jakobsson-invitro-bulk-rnaseq-microglia gs://asap-uat-team-jakobsson-invitro-bulk-rnaseq-microglia gs://asap-curated-team-jakobsson-invitro-bulk-rnaseq-microglia v3.0.2 v4.0.0 v3.0.2 v1.0 v3.3 v4.0.0 v1.0 v3.3" data-tags="invitro||invitro-bulk-rnaseq||jakobsson">
      <td><code>jakobsson-invitro-bulk-rnaseq-microglia</code></td>
      <td>Bulk RNAseq of microglia in vitro cultures</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-jakobsson-invitro-bulk-rnaseq-microglia-19">View</button></td>
    </tr>
    <tr id="dataset-detail-jakobsson-invitro-bulk-rnaseq-microglia-19" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Bulk RNAseq of microglia in vitro cultures</h3>
          <p><strong>Dataset ID:</strong> <code>jakobsson-invitro-bulk-rnaseq-microglia</code></p>
          <p><strong>Description:</strong> This dataset includes bulk RNAseq (2 x 150bps reads; Illumina TruSeq Stranded mRNA library prep kit with poly-A selection) of differentiated human pluripotent stem cells (hPSCs) into microglia. Briefly, hES (H9) and hiPSCs (KOLF2.1) underwent mesodermal induction via embryoid body formation, followed by hemogenic endothelium induction and myeloid differentiation to generate primitive monocyte-like precursors. These precursors were then matured into microglia by supplementing with key neuron-derived factors that promote microglial identity, thereby recapitulating human microglia in monoculture. A detailed protocol can be found at doi: dx.doi.org/10.17504/protocols.io.14egnr8ezl5d/v1.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17149290" target="_blank" rel="noopener">10.5281/zenodo.17149290</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">invitro</span> <span class="tag-pill">invitro-bulk-rnaseq</span> <span class="tag-pill">jakobsson</span></p>
          <p><strong>Keywords:</strong> invitro-bulk-rnaseq, invitro, jakobsson</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.2</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-jakobsson-invitro-bulk-rnaseq-microglia</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-jakobsson-invitro-bulk-rnaseq-microglia</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-jakobsson-invitro-bulk-rnaseq-microglia</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-jakobsson-invitro-bulk-rnaseq-microglia</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-jakobsson-pmdbs-bulk-rnaseq-20" data-search="jakobsson-pmdbs-bulk-rnaseq deep bulk rnaseq of neurological controls and pd brains human post-mortem brain tissue from donors with lewy body pathology and neurologically healthy controls was sourced from the cambridge brain bank under london–bloomsbury research ethics committee (rec reference no. 16/lo/0508). donors with lewy body pathology (n=25) had a clinical diagnosis of parkinson&#x27;s disease and were compared to an age- and sex-matched group of neurologically healthy control donors (n=18) who had no history of neurological illness. a neuropathologist assessed all cases for lewy body pathology braak staging, co-existing proteinopathies and other pathologies. fresh frozen tissue was sampled from sn,  put, amy, and pfc at the level of brodmann area 46 (pfc). a 3 mm3 tissue piece was cut from the same tissue block that had been used for snrna sequencing and disrupted using a tissuelyser (qiagen). a steel bead and rlt buffer with -mercaptoethanol was added to the tissuelyser and shaken at 30 hz for 2 minutes. total rna was isolated from the disrupted tissue using the rneasy mini kit (qiagen; rrid). the sequencing libraries were then generated using illumina truseq stranded mrna library prep kit (with poly-a selection) and sequenced on a novaseq6000 or novaseq x plus (2 x 150 paired end). basecalling and sample-specific fastq files were done using illumina&#x27;s bcl2fastq  in default parameters. reads were uniquely mapped to hg38 reference genome using star aligner (version 2.7.8a; ref; rfid, --outfiltermultimapnmax 1, --outfiltermismatchnoverlmax 0.03).  te and gene quantification was performed using featurecounts (subread package version 1.6.3; ref; rfid -s 2) and gencode annotation version 38, repeatmasker (open-4.0.5, filtered from trnas, simple repeats, small rnas, and low-complexity regions), or retrotector predictions annotation. pmdbs-bulk-rnaseq cc-by-4.0 10.5281/zenodo.16929448 jakobsson other-pmdbs pmdbs-bulk-rnaseq pmdbs-bulk-rnaseq other-pmdbs jakobsson gs://asap-raw-team-jakobsson-pmdbs-bulk-rnaseq gs://asap-dev-team-jakobsson-pmdbs-bulk-rnaseq gs://asap-uat-team-jakobsson-pmdbs-bulk-rnaseq gs://asap-curated-team-jakobsson-pmdbs-bulk-rnaseq v3.0.0 v4.0.0 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3" data-tags="jakobsson||other-pmdbs||pmdbs-bulk-rnaseq">
      <td><code>jakobsson-pmdbs-bulk-rnaseq</code></td>
      <td>Deep bulk RNAseq of neurological controls and PD brains</td>
      <td>pmdbs-bulk-rnaseq</td>
      <td>v1.0</td>
      <td>v4.0.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-jakobsson-pmdbs-bulk-rnaseq-20">View</button></td>
    </tr>
    <tr id="dataset-detail-jakobsson-pmdbs-bulk-rnaseq-20" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Deep bulk RNAseq of neurological controls and PD brains</h3>
          <p><strong>Dataset ID:</strong> <code>jakobsson-pmdbs-bulk-rnaseq</code></p>
          <p><strong>Description:</strong> Human post-mortem brain tissue from donors with Lewy Body pathology and neurologically healthy controls was sourced from the Cambridge Brain Bank under London–Bloomsbury Research Ethics Committee (REC reference no. 16/LO/0508). Donors with Lewy Body pathology (n=25) had a clinical diagnosis of Parkinson&#x27;s disease and were compared to an age- and sex-matched group of neurologically healthy control donors (n=18) who had no history of neurological illness. A neuropathologist assessed all cases for Lewy Body pathology Braak staging, co-existing proteinopathies and other pathologies. Fresh frozen tissue was sampled from SN,  PUT, AMY, and PFC at the level of Brodmann area 46 (PFC). A 3 mm3 tissue piece was cut from the same tissue block that had been used for snRNA sequencing and disrupted using a Tissuelyser (Qiagen). A steel bead and RLT buffer with -mercaptoethanol was added to the Tissuelyser and shaken at 30 Hz for 2 minutes. Total RNA was isolated from the disrupted tissue using the RNeasy Mini Kit (Qiagen; RRID). The sequencing libraries were then generated using Illumina TruSeq Stranded mRNA library prep kit (with poly-A selection) and sequenced on a NovaSeq6000 or Novaseq X plus (2 x 150 paired end). Basecalling and sample-specific fastq files were done using Illumina&#x27;s bcl2fastq  in default parameters. Reads were uniquely mapped to hg38 reference genome using STAR aligner (version 2.7.8a; REF; RFID, --outFilterMultimapNmax 1, --outFilterMismatchNoverLmax 0.03).  TE and gene quantification was performed using featureCounts (subread package version 1.6.3; REF; RFID -s 2) and gencode annotation version 38, repeatmasker (open-4.0.5, filtered from tRNAs, simple repeats, small RNAs, and low-complexity regions), or retrotector predictions annotation.</p>
          <p><strong>Collection:</strong> pmdbs-bulk-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16929448" target="_blank" rel="noopener">10.5281/zenodo.16929448</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">jakobsson</span> <span class="tag-pill">other-pmdbs</span> <span class="tag-pill">pmdbs-bulk-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs-bulk-rnaseq, other-pmdbs, jakobsson</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-jakobsson-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-jakobsson-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-jakobsson-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-jakobsson-pmdbs-bulk-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-jakobsson-pmdbs-sn-rnaseq-21" data-search="jakobsson-pmdbs-sn-rnaseq single nuclei sequencing of brain regions from healthy and parkinson&#x27;s disease individuals we performed single nuclei rna sequencing of postmortem pd and control brain tissue of four different brain regions (substantia nigra, putamen, amygdala, and prefrontal cortex). briefly, 8500 nuclei were facs sorted from approximately 2 mm3 of tissue. single nuclei rnaseq libraries were prepared using 10x genomics platform for single cell 3&#x27; sequencing. sequencing libraries are prepared by fragmentation, end repair and a tailing followed by sample index pcr. to process the data, fastq files were processed using cell ranger, aligning and quantifying for hg38. intronic reads were also quantified. pmdbs-sc-rnaseq cc-by-4.0 10.5281/zenodo.15162834 jakobsson pmdbs-other pmdbs-sc-rnaseq pmdbs-sc-rnaseq pmdbs-other jakobsson gs://asap-raw-team-jakobsson-pmdbs-sn-rnaseq gs://asap-dev-team-jakobsson-pmdbs-sn-rnaseq gs://asap-uat-team-jakobsson-pmdbs-sn-rnaseq gs://asap-curated-team-jakobsson-pmdbs-sn-rnaseq v1.0.0 v2.0.0 v2.0.1 v3.0.0 v4.0.0 v4.1.0 v1.0.0 v1.0 v2.1 v2.0.0 v1.0 v3.0 v2.0.1 v2.0 v3.1 v3.0.0 v2.0 v3.2 v4.0.0 v2.0 v3.3 v4.1.0 v2.1 v3.3" data-tags="jakobsson||pmdbs-other||pmdbs-sc-rnaseq">
      <td><code>jakobsson-pmdbs-sn-rnaseq</code></td>
      <td>Single nuclei sequencing of brain regions from healthy and Parkinson&#x27;s Disease individuals</td>
      <td>pmdbs-sc-rnaseq</td>
      <td>v2.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-jakobsson-pmdbs-sn-rnaseq-21">View</button></td>
    </tr>
    <tr id="dataset-detail-jakobsson-pmdbs-sn-rnaseq-21" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single nuclei sequencing of brain regions from healthy and Parkinson&#x27;s Disease individuals</h3>
          <p><strong>Dataset ID:</strong> <code>jakobsson-pmdbs-sn-rnaseq</code></p>
          <p><strong>Description:</strong> We performed single nuclei RNA sequencing of postmortem PD and control brain tissue of four different brain regions (substantia nigra, putamen, amygdala, and prefrontal cortex). Briefly, 8500 nuclei were FACS sorted from approximately 2 mm3 of tissue. Single nuclei RNAseq libraries were prepared using 10X genomics platform for single cell 3&#x27; sequencing. Sequencing libraries are prepared by fragmentation, end repair and a tailing followed by sample index PCR. To process the data, FASTQ files were processed using Cell Ranger, aligning and quantifying for hg38. Intronic reads were also quantified.</p>
          <p><strong>Collection:</strong> pmdbs-sc-rnaseq</p>
          <p><strong>Current dataset version:</strong> v2.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.15162834" target="_blank" rel="noopener">10.5281/zenodo.15162834</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">jakobsson</span> <span class="tag-pill">pmdbs-other</span> <span class="tag-pill">pmdbs-sc-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs-sc-rnaseq, pmdbs-other, jakobsson</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v2.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v2.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v2.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.1</td>
                <td>v2.0</td>
                <td>v3.1</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v1.0</td>
                <td>v3.0</td>
              </tr>
              <tr>
                <td>v1.0.0</td>
                <td>v1.0</td>
                <td>v2.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-jakobsson-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-jakobsson-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-jakobsson-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-jakobsson-pmdbs-sn-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet-22" data-search="lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet bulk rna-seq analysis of the striatum in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, striatal tissue was collected for bulk rna-seq analysis. each experimental group contained biological replicates (n = 4 per group). na cc-by-4.0 10.5281/zenodo.18273802 bulk-rnaseq lee mouse mouse bulk-rnaseq lee gs://asap-raw-team-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet gs://asap-dev-team-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet gs://asap-uat-team-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet gs://asap-curated-team-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet v4.0.1 v4.0.1 v1.0 v4.1" data-tags="bulk-rnaseq||lee||mouse">
      <td><code>lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet</code></td>
      <td>Bulk RNA-seq analysis of the striatum in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet-22">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet-22" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Bulk RNA-seq analysis of the striatum in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, striatal tissue was collected for bulk RNA-seq analysis. Each experimental group contained biological replicates (n = 4 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.1</p>
          <p><strong>Latest CDE version:</strong> v4.1</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273802" target="_blank" rel="noopener">10.5281/zenodo.18273802</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">bulk-rnaseq</span> <span class="tag-pill">lee</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, bulk-rnaseq, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.1</td>
                <td>v1.0</td>
                <td>v4.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-bulk-rnaseq-striatum-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-liver-bulk-rnaseq-g2019s-23" data-search="lee-mouse-liver-bulk-rnaseq-g2019s bulk rna-seq analysis of the liver in g2019s lrrk2 knockin mice the liver was collected from g2019s lrrk2 knockin mice and their wild-type littermates (3-5 months old) for bulk rna-seq analysis. each experimental group contained biological replicates (n = 4 per group). na cc-by-4.0 10.5281/zenodo.18273810 bulk-rnaseq lee liver mouse mouse liver bulk-rnaseq lee gs://asap-raw-team-lee-mouse-liver-bulk-rnaseq-g2019s gs://asap-dev-team-lee-mouse-liver-bulk-rnaseq-g2019s gs://asap-uat-team-lee-mouse-liver-bulk-rnaseq-g2019s gs://asap-curated-team-lee-mouse-liver-bulk-rnaseq-g2019s v4.0.1 v4.0.1 v1.0 v4.1" data-tags="bulk-rnaseq||lee||liver||mouse">
      <td><code>lee-mouse-liver-bulk-rnaseq-g2019s</code></td>
      <td>Bulk RNA-seq analysis of the liver in G2019S LRRK2 knockin mice</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-liver-bulk-rnaseq-g2019s-23">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-liver-bulk-rnaseq-g2019s-23" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Bulk RNA-seq analysis of the liver in G2019S LRRK2 knockin mice</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-liver-bulk-rnaseq-g2019s</code></p>
          <p><strong>Description:</strong> The liver was collected from G2019S LRRK2 knockin mice and their wild-type littermates (3-5 months old) for bulk RNA-seq analysis. Each experimental group contained biological replicates (n = 4 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.1</p>
          <p><strong>Latest CDE version:</strong> v4.1</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273810" target="_blank" rel="noopener">10.5281/zenodo.18273810</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">bulk-rnaseq</span> <span class="tag-pill">lee</span> <span class="tag-pill">liver</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, liver, bulk-rnaseq, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.1</td>
                <td>v1.0</td>
                <td>v4.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-liver-bulk-rnaseq-g2019s</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-liver-bulk-rnaseq-g2019s</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-liver-bulk-rnaseq-g2019s</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-liver-bulk-rnaseq-g2019s</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-l-kidney-g2019s-hf-diet-24" data-search="lee-mouse-ms-l-kidney-g2019s-hf-diet untargeted lipidomic profiling of the kidney in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized, homogenized and processed using the bligh-dyer method. lipid identifications were assigned using lipidsearch (v5.0, thermo fisher scientific) which was used to generate a compound list, and lipid peak areas were quantified in skyline. each experimental group contained biological replicates (n = 5-6 per group). na cc-by-4.0 10.5281/zenodo.18273858 kidney lee mouse mouse kidney lee gs://asap-raw-team-lee-mouse-ms-l-kidney-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-l-kidney-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-l-kidney-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-l-kidney-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="kidney||lee||mouse">
      <td><code>lee-mouse-ms-l-kidney-g2019s-hf-diet</code></td>
      <td>Untargeted lipidomic profiling of the kidney in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-l-kidney-g2019s-hf-diet-24">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-l-kidney-g2019s-hf-diet-24" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Untargeted lipidomic profiling of the kidney in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-l-kidney-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized, homogenized and processed using the Bligh-Dyer method. Lipid identifications were assigned using LipidSearch (v5.0, Thermo Fisher Scientific) which was used to generate a compound list, and lipid peak areas were quantified in Skyline. Each experimental group contained biological replicates (n = 5-6 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273858" target="_blank" rel="noopener">10.5281/zenodo.18273858</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">kidney</span> <span class="tag-pill">lee</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, kidney, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-l-kidney-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-l-kidney-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-l-kidney-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-l-kidney-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-l-liver-g2019s-hf-diet-25" data-search="lee-mouse-ms-l-liver-g2019s-hf-diet untargeted lipidomic profiling of the liver in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized, homogenized and processed using the bligh-dyer method. lipid identifications were assigned using lipidsearch (v5.0, thermo fisher scientific) which was used to generate a compound list, and lipid peak areas were quantified in skyline. each experimental group contained biological replicates (n = 6 per group). na cc-by-4.0 10.5281/zenodo.18273844 lee liver mouse mouse liver lee gs://asap-raw-team-lee-mouse-ms-l-liver-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-l-liver-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-l-liver-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-l-liver-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||liver||mouse">
      <td><code>lee-mouse-ms-l-liver-g2019s-hf-diet</code></td>
      <td>Untargeted lipidomic profiling of the liver in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-l-liver-g2019s-hf-diet-25">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-l-liver-g2019s-hf-diet-25" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Untargeted lipidomic profiling of the liver in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-l-liver-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized, homogenized and processed using the Bligh-Dyer method. Lipid identifications were assigned using LipidSearch (v5.0, Thermo Fisher Scientific) which was used to generate a compound list, and lipid peak areas were quantified in Skyline. Each experimental group contained biological replicates (n = 6 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273844" target="_blank" rel="noopener">10.5281/zenodo.18273844</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">liver</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, liver, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-l-liver-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-l-liver-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-l-liver-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-l-liver-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-l-lung-g2019s-hf-diet-26" data-search="lee-mouse-ms-l-lung-g2019s-hf-diet untargeted lipidomic profiling of the lung in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized, homogenized and processed using the bligh-dyer method. lipid identifications were assigned using lipidsearch (v5.0, thermo fisher scientific) which was used to generate a compound list, and lipid peak areas were quantified in skyline. each experimental group contained biological replicates (n = 5-6 per group). na cc-by-4.0 10.5281/zenodo.18273852 lee lung mouse mouse lung lee gs://asap-raw-team-lee-mouse-ms-l-lung-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-l-lung-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-l-lung-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-l-lung-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||lung||mouse">
      <td><code>lee-mouse-ms-l-lung-g2019s-hf-diet</code></td>
      <td>Untargeted lipidomic profiling of the lung in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-l-lung-g2019s-hf-diet-26">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-l-lung-g2019s-hf-diet-26" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Untargeted lipidomic profiling of the lung in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-l-lung-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized, homogenized and processed using the Bligh-Dyer method. Lipid identifications were assigned using LipidSearch (v5.0, Thermo Fisher Scientific) which was used to generate a compound list, and lipid peak areas were quantified in Skyline. Each experimental group contained biological replicates (n = 5-6 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273852" target="_blank" rel="noopener">10.5281/zenodo.18273852</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">lung</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, lung, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-l-lung-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-l-lung-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-l-lung-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-l-lung-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-l-plasma-g2019s-hf-diet-27" data-search="lee-mouse-ms-l-plasma-g2019s-hf-diet untargeted lipidomic profiling of the plasma in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, and whole blood was collected from cardiac puncture. 50 μl plasma from each mouse was split and processed using the bligh-dyer method. lipid identifications were assigned using lipidsearch (v5.0, thermo fisher scientific) which was used to generate a compound list, and lipid peak areas were quantified in skyline. each experimental group contained biological replicates (n = 6 per group). na cc-by-4.0 10.5281/zenodo.18273840 lee mouse plasma mouse plasma lee gs://asap-raw-team-lee-mouse-ms-l-plasma-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-l-plasma-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-l-plasma-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-l-plasma-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||mouse||plasma">
      <td><code>lee-mouse-ms-l-plasma-g2019s-hf-diet</code></td>
      <td>Untargeted lipidomic profiling of the plasma in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-l-plasma-g2019s-hf-diet-27">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-l-plasma-g2019s-hf-diet-27" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Untargeted lipidomic profiling of the plasma in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-l-plasma-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, and whole blood was collected from cardiac puncture. 50 μL plasma from each mouse was split and processed using the Bligh-Dyer method. Lipid identifications were assigned using LipidSearch (v5.0, Thermo Fisher Scientific) which was used to generate a compound list, and lipid peak areas were quantified in Skyline. Each experimental group contained biological replicates (n = 6 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273840" target="_blank" rel="noopener">10.5281/zenodo.18273840</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">mouse</span> <span class="tag-pill">plasma</span></p>
          <p><strong>Keywords:</strong> mouse, plasma, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-l-plasma-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-l-plasma-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-l-plasma-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-l-plasma-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-l-striatum-g2019s-hf-diet-28" data-search="lee-mouse-ms-l-striatum-g2019s-hf-diet untargeted lipidomic profiling of the striatum in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized, homogenized and processed using the bligh-dyer method. lipid identifications were assigned using lipidsearch (v5.0, thermo fisher scientific) which was used to generate a compound list, and lipid peak areas were quantified in skyline. each experimental group contained biological replicates (n = 5-6 per group). na cc-by-4.0 10.5281/zenodo.18273848 lee mouse striatum mouse striatum lee gs://asap-raw-team-lee-mouse-ms-l-striatum-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-l-striatum-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-l-striatum-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-l-striatum-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||mouse||striatum">
      <td><code>lee-mouse-ms-l-striatum-g2019s-hf-diet</code></td>
      <td>Untargeted lipidomic profiling of the striatum in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-l-striatum-g2019s-hf-diet-28">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-l-striatum-g2019s-hf-diet-28" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Untargeted lipidomic profiling of the striatum in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-l-striatum-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized, homogenized and processed using the Bligh-Dyer method. Lipid identifications were assigned using LipidSearch (v5.0, Thermo Fisher Scientific) which was used to generate a compound list, and lipid peak areas were quantified in Skyline. Each experimental group contained biological replicates (n = 5-6 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273848" target="_blank" rel="noopener">10.5281/zenodo.18273848</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">mouse</span> <span class="tag-pill">striatum</span></p>
          <p><strong>Keywords:</strong> mouse, striatum, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-l-striatum-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-l-striatum-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-l-striatum-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-l-striatum-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-mb-kidney-g2019s-hf-diet-29" data-search="lee-mouse-ms-mb-kidney-g2019s-hf-diet targeted metabolomic profiling of the kidney in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized, homogenized and processed using the bligh-dyer method. targeted metabolomics peak picking and integration were conducted in skyline (v25.1) using accurate mass ms1, ms2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. each experimental group contained biological replicates (n = 6 per group). na cc-by-4.0 10.5281/zenodo.18273834 kidney lee mouse mouse kidney lee gs://asap-raw-team-lee-mouse-ms-mb-kidney-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-mb-kidney-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-mb-kidney-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-mb-kidney-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="kidney||lee||mouse">
      <td><code>lee-mouse-ms-mb-kidney-g2019s-hf-diet</code></td>
      <td>Targeted metabolomic profiling of the kidney in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-mb-kidney-g2019s-hf-diet-29">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-mb-kidney-g2019s-hf-diet-29" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Targeted metabolomic profiling of the kidney in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-mb-kidney-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized, homogenized and processed using the Bligh-Dyer method. Targeted metabolomics peak picking and integration were conducted in Skyline (v25.1) using accurate mass MS1, MS2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. Raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. Each experimental group contained biological replicates (n = 6 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273834" target="_blank" rel="noopener">10.5281/zenodo.18273834</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">kidney</span> <span class="tag-pill">lee</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, kidney, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-mb-kidney-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-mb-kidney-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-mb-kidney-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-mb-kidney-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-mb-liver-g2019s-hf-diet-30" data-search="lee-mouse-ms-mb-liver-g2019s-hf-diet targeted metabolomic profiling of the liver in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized, homogenized and processed using the bligh-dyer method. targeted metabolomics peak picking and integration were conducted in skyline (v25.1) using accurate mass ms1, ms2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. each experimental group contained biological replicates (n = 6 per group). na cc-by-4.0 10.5281/zenodo.18273822 lee liver mouse mouse liver lee gs://asap-raw-team-lee-mouse-ms-mb-liver-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-mb-liver-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-mb-liver-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-mb-liver-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||liver||mouse">
      <td><code>lee-mouse-ms-mb-liver-g2019s-hf-diet</code></td>
      <td>Targeted metabolomic profiling of the liver in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-mb-liver-g2019s-hf-diet-30">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-mb-liver-g2019s-hf-diet-30" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Targeted metabolomic profiling of the liver in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-mb-liver-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized, homogenized and processed using the Bligh-Dyer method. Targeted metabolomics peak picking and integration were conducted in Skyline (v25.1) using accurate mass MS1, MS2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. Raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. Each experimental group contained biological replicates (n = 6 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273822" target="_blank" rel="noopener">10.5281/zenodo.18273822</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">liver</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, liver, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-mb-liver-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-mb-liver-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-mb-liver-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-mb-liver-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-mb-lung-g2019s-hf-diet-31" data-search="lee-mouse-ms-mb-lung-g2019s-hf-diet targeted metabolomic profiling of the lung in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized, homogenized and processed using the bligh-dyer method. targeted metabolomics peak picking and integration were conducted in skyline (v25.1) using accurate mass ms1, ms2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. each experimental group contained biological replicates (n = 5-6 per group). na cc-by-4.0 10.5281/zenodo.18273832 lee lung mouse mouse lung lee gs://asap-raw-team-lee-mouse-ms-mb-lung-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-mb-lung-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-mb-lung-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-mb-lung-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||lung||mouse">
      <td><code>lee-mouse-ms-mb-lung-g2019s-hf-diet</code></td>
      <td>Targeted metabolomic profiling of the lung in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-mb-lung-g2019s-hf-diet-31">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-mb-lung-g2019s-hf-diet-31" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Targeted metabolomic profiling of the lung in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-mb-lung-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized, homogenized and processed using the Bligh-Dyer method. Targeted metabolomics peak picking and integration were conducted in Skyline (v25.1) using accurate mass MS1, MS2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. Raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. Each experimental group contained biological replicates (n = 5-6 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273832" target="_blank" rel="noopener">10.5281/zenodo.18273832</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">lung</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, lung, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-mb-lung-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-mb-lung-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-mb-lung-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-mb-lung-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant-32" data-search="lee-mouse-ms-mb-midbrain-g2019s-nuc-quant nucleoside quantification in the ventral midbrain of g2019s lrrk2 knockin mice g2019s lrrk2 knockin mice and their wild-type littermates (3-5 months old) were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized, homogenized and processed using the bligh-dyer method. absolute nucleoside quantitation was accomplished by running an external calibration curve with the samples. the stock mix contained deoxyadenosine (da), deoxycytidine (dc), deoxyguanosine (dg), deoxythymidine (dt), and deoxyuridine (du). targeted metabolomics peak picking and integration were conducted in skyline (v25.1) using accurate mass ms1, ms2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. each experimental group contained biological replicates (n = 9 per group). na cc-by-4.0 10.5281/zenodo.18273870 brain lee midbrain mouse mouse brain midbrain lee gs://asap-raw-team-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant gs://asap-dev-team-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant gs://asap-uat-team-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant gs://asap-curated-team-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant v4.1.0 v4.1.0 v1.0 v4.3" data-tags="brain||lee||midbrain||mouse">
      <td><code>lee-mouse-ms-mb-midbrain-g2019s-nuc-quant</code></td>
      <td>Nucleoside quantification in the ventral midbrain of G2019S LRRK2 knockin mice</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant-32">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant-32" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Nucleoside quantification in the ventral midbrain of G2019S LRRK2 knockin mice</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-mb-midbrain-g2019s-nuc-quant</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates (3-5 months old) were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized, homogenized and processed using the Bligh-Dyer method. Absolute nucleoside quantitation was accomplished by running an external calibration curve with the samples. The stock mix contained Deoxyadenosine (dA), Deoxycytidine (dC), Deoxyguanosine (dG), Deoxythymidine (dT), and Deoxyuridine (dU). Targeted metabolomics peak picking and integration were conducted in Skyline (v25.1) using accurate mass MS1, MS2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. Raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. Each experimental group contained biological replicates (n = 9 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273870" target="_blank" rel="noopener">10.5281/zenodo.18273870</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">brain</span> <span class="tag-pill">lee</span> <span class="tag-pill">midbrain</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, brain, midbrain, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-mb-midbrain-g2019s-nuc-quant</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-mb-plasma-g2019s-hf-diet-33" data-search="lee-mouse-ms-mb-plasma-g2019s-hf-diet targeted metabolomic profiling of the plasma in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, and whole blood was collected from cardiac puncture. 50 μl plasma from each mouse was split and processed using the bligh-dyer method. targeted metabolomics peak picking and integration were conducted in skyline (v25.1) using accurate mass ms1, ms2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. each experimental group contained biological replicates (n = 6 per group). na cc-by-4.0 10.5281/zenodo.18273818 lee mouse plasma mouse plasma lee gs://asap-raw-team-lee-mouse-ms-mb-plasma-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-mb-plasma-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-mb-plasma-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-mb-plasma-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||mouse||plasma">
      <td><code>lee-mouse-ms-mb-plasma-g2019s-hf-diet</code></td>
      <td>Targeted metabolomic profiling of the plasma in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-mb-plasma-g2019s-hf-diet-33">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-mb-plasma-g2019s-hf-diet-33" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Targeted metabolomic profiling of the plasma in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-mb-plasma-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, and whole blood was collected from cardiac puncture. 50 μL plasma from each mouse was split and processed using the Bligh-Dyer method. Targeted metabolomics peak picking and integration were conducted in Skyline (v25.1) using accurate mass MS1, MS2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. Raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. Each experimental group contained biological replicates (n = 6 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273818" target="_blank" rel="noopener">10.5281/zenodo.18273818</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">mouse</span> <span class="tag-pill">plasma</span></p>
          <p><strong>Keywords:</strong> mouse, plasma, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-mb-plasma-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-mb-plasma-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-mb-plasma-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-mb-plasma-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-mb-plasma-g2019s-nuc-quant-34" data-search="lee-mouse-ms-mb-plasma-g2019s-nuc-quant nucleoside quantification in the plasma of g2019s lrrk2 knockin mice g2019s lrrk2 knockin mice and their wild-type littermates (3-5 months old) were anesthetized with an isoflurane vaporizer, and whole blood was collected from cardiac puncture. 50 μl plasma from each mouse was split and processed using the bligh-dyer method. absolute nucleoside quantitation was accomplished by running an external calibration curve with the samples. the stock mix contained deoxyadenosine (da), deoxycytidine (dc), deoxyguanosine (dg), deoxythymidine (dt), and deoxyuridine (du). targeted metabolomics peak picking and integration were conducted in skyline (v25.1) using accurate mass ms1, ms2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. each experimental group contained biological replicates (n =8-9 per group). na cc-by-4.0 10.5281/zenodo.18273863 lee mouse plasma mouse plasma lee gs://asap-raw-team-lee-mouse-ms-mb-plasma-g2019s-nuc-quant gs://asap-dev-team-lee-mouse-ms-mb-plasma-g2019s-nuc-quant gs://asap-uat-team-lee-mouse-ms-mb-plasma-g2019s-nuc-quant gs://asap-curated-team-lee-mouse-ms-mb-plasma-g2019s-nuc-quant v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||mouse||plasma">
      <td><code>lee-mouse-ms-mb-plasma-g2019s-nuc-quant</code></td>
      <td>Nucleoside quantification in the plasma of G2019S LRRK2 knockin mice</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-mb-plasma-g2019s-nuc-quant-34">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-mb-plasma-g2019s-nuc-quant-34" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Nucleoside quantification in the plasma of G2019S LRRK2 knockin mice</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-mb-plasma-g2019s-nuc-quant</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates (3-5 months old) were anesthetized with an isoflurane vaporizer, and whole blood was collected from cardiac puncture. 50 μL plasma from each mouse was split and processed using the Bligh-Dyer method. Absolute nucleoside quantitation was accomplished by running an external calibration curve with the samples. The stock mix contained Deoxyadenosine (dA), Deoxycytidine (dC), Deoxyguanosine (dG), Deoxythymidine (dT), and Deoxyuridine (dU). Targeted metabolomics peak picking and integration were conducted in Skyline (v25.1) using accurate mass MS1, MS2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. Raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. Each experimental group contained biological replicates (n =8-9 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273863" target="_blank" rel="noopener">10.5281/zenodo.18273863</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">mouse</span> <span class="tag-pill">plasma</span></p>
          <p><strong>Keywords:</strong> mouse, plasma, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-mb-plasma-g2019s-nuc-quant</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-mb-plasma-g2019s-nuc-quant</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-mb-plasma-g2019s-nuc-quant</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-mb-plasma-g2019s-nuc-quant</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-mb-striatum-g2019s-hf-diet-35" data-search="lee-mouse-ms-mb-striatum-g2019s-hf-diet targeted metabolomic profiling of the striatum in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized, homogenized and processed using the bligh-dyer method. targeted metabolomics peak picking and integration were conducted in skyline (v25.1) using accurate mass ms1, ms2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. each experimental group contained biological replicates (n = 5-6 per group). na cc-by-4.0 10.5281/zenodo.18273824 lee mouse striatum mouse striatum lee gs://asap-raw-team-lee-mouse-ms-mb-striatum-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-mb-striatum-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-mb-striatum-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-mb-striatum-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||mouse||striatum">
      <td><code>lee-mouse-ms-mb-striatum-g2019s-hf-diet</code></td>
      <td>Targeted metabolomic profiling of the striatum in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-mb-striatum-g2019s-hf-diet-35">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-mb-striatum-g2019s-hf-diet-35" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Targeted metabolomic profiling of the striatum in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-mb-striatum-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized, homogenized and processed using the Bligh-Dyer method. Targeted metabolomics peak picking and integration were conducted in Skyline (v25.1) using accurate mass MS1, MS2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. Raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. Each experimental group contained biological replicates (n = 5-6 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273824" target="_blank" rel="noopener">10.5281/zenodo.18273824</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">mouse</span> <span class="tag-pill">striatum</span></p>
          <p><strong>Keywords:</strong> mouse, striatum, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-mb-striatum-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-mb-striatum-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-mb-striatum-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-mb-striatum-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-mb-striatum-g2019s-nuc-quant-36" data-search="lee-mouse-ms-mb-striatum-g2019s-nuc-quant nucleoside quantification in the striatum of g2019s lrrk2 knockin mice g2019s lrrk2 knockin mice and their wild-type littermates (3-5 months old) were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized, homogenized and processed using the bligh-dyer method. absolute nucleoside quantitation was accomplished by running an external calibration curve with the samples. the stock mix contained deoxyadenosine (da), deoxycytidine (dc), deoxyguanosine (dg), deoxythymidine (dt), and deoxyuridine (du). targeted metabolomics peak picking and integration were conducted in skyline (v25.1) using accurate mass ms1, ms2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. each experimental group contained biological replicates (n = 9 per group). na cc-by-4.0 10.5281/zenodo.18273868 lee mouse striatum mouse striatum lee gs://asap-raw-team-lee-mouse-ms-mb-striatum-g2019s-nuc-quant gs://asap-dev-team-lee-mouse-ms-mb-striatum-g2019s-nuc-quant gs://asap-uat-team-lee-mouse-ms-mb-striatum-g2019s-nuc-quant gs://asap-curated-team-lee-mouse-ms-mb-striatum-g2019s-nuc-quant v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||mouse||striatum">
      <td><code>lee-mouse-ms-mb-striatum-g2019s-nuc-quant</code></td>
      <td>Nucleoside quantification in the striatum of G2019S LRRK2 knockin mice</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-mb-striatum-g2019s-nuc-quant-36">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-mb-striatum-g2019s-nuc-quant-36" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Nucleoside quantification in the striatum of G2019S LRRK2 knockin mice</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-mb-striatum-g2019s-nuc-quant</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates (3-5 months old) were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized, homogenized and processed using the Bligh-Dyer method. Absolute nucleoside quantitation was accomplished by running an external calibration curve with the samples. The stock mix contained Deoxyadenosine (dA), Deoxycytidine (dC), Deoxyguanosine (dG), Deoxythymidine (dT), and Deoxyuridine (dU). Targeted metabolomics peak picking and integration were conducted in Skyline (v25.1) using accurate mass MS1, MS2 fragmentation pattern matching, and retention time derived from analytical standards run through each chromatography method. Raw data files for all samples of a given experiment were imported and metabolite peaks were auto-integrated based standard verified m/z, precursor adducts, and retention times for all metabolites of interest. Each experimental group contained biological replicates (n = 9 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273868" target="_blank" rel="noopener">10.5281/zenodo.18273868</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">mouse</span> <span class="tag-pill">striatum</span></p>
          <p><strong>Keywords:</strong> mouse, striatum, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-mb-striatum-g2019s-nuc-quant</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-mb-striatum-g2019s-nuc-quant</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-mb-striatum-g2019s-nuc-quant</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-mb-striatum-g2019s-nuc-quant</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-ms-p-lung-g2019s-hf-diet-37" data-search="lee-mouse-ms-p-lung-g2019s-hf-diet global proteomic analysis of the lung in g2019s lrrk2 knockin mice under a specialized diet g2019s lrrk2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. at that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). mice remained on their respective diets for an additional five months. at 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. frozen tissues were cryopulverized and homogenized. protein were digested and dried down before resuspension for lc-ms/ms analysis. dia data was processed in spectronaut (version 18, biognosys, switzerland) using direct dia. data was searched against the mus musculus proteome, including expected mutations. the manufacturer&#x27;s default parameters were used. each experimental group contained biological replicates (n = 4 per group). na cc-by-4.0 10.5281/zenodo.18273812 lee lung mouse mouse lung lee gs://asap-raw-team-lee-mouse-ms-p-lung-g2019s-hf-diet gs://asap-dev-team-lee-mouse-ms-p-lung-g2019s-hf-diet gs://asap-uat-team-lee-mouse-ms-p-lung-g2019s-hf-diet gs://asap-curated-team-lee-mouse-ms-p-lung-g2019s-hf-diet v4.1.0 v4.1.0 v1.0 v4.3" data-tags="lee||lung||mouse">
      <td><code>lee-mouse-ms-p-lung-g2019s-hf-diet</code></td>
      <td>Global proteomic analysis of the lung in G2019S LRRK2 knockin mice under a specialized diet</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-ms-p-lung-g2019s-hf-diet-37">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-ms-p-lung-g2019s-hf-diet-37" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Global proteomic analysis of the lung in G2019S LRRK2 knockin mice under a specialized diet</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-ms-p-lung-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> G2019S LRRK2 knockin mice and their wild-type littermates were maintained on a normal chow diet (23.7% kcal from fat) for the first 11 months of life. At that time, animals were randomly assigned to either a high-fat diet group (60% kcal from fat) or a control diet group (10% kcal from fat). Mice remained on their respective diets for an additional five months. At 16 months of age, mice were anesthetized with an isoflurane vaporizer, tissue were then collected and immediately snap frozen in liquid nitrogen. Frozen tissues were cryopulverized and homogenized. Protein were digested and dried down before resuspension for LC-MS/MS analysis. DIA data was processed in Spectronaut (version 18, Biognosys, Switzerland) using direct DIA. Data was searched against the Mus musculus proteome, including expected mutations. The manufacturer&#x27;s default parameters were used. Each experimental group contained biological replicates (n = 4 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273812" target="_blank" rel="noopener">10.5281/zenodo.18273812</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">lung</span> <span class="tag-pill">mouse</span></p>
          <p><strong>Keywords:</strong> mouse, lung, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-ms-p-lung-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-ms-p-lung-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-ms-p-lung-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-ms-p-lung-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet-38" data-search="lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet bulk rna-seq analysis of the liver in g2019s lrrk2 knockin mice the liver was collected from g2019s lrrk2 knockin mice and their wild-type littermates (3-5 months old) for bulk rna-seq analysis. each experimental group contained biological replicates (n = 4 per group). na cc-by-4.0 10.5281/zenodo.18273808 lee mouse sn-rnaseq mouse sn-rnaseq lee gs://asap-raw-team-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet gs://asap-dev-team-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet gs://asap-uat-team-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet gs://asap-curated-team-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet v4.0.1 v4.0.1 v1.0 v4.1" data-tags="lee||mouse||sn-rnaseq">
      <td><code>lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet</code></td>
      <td>Bulk RNA-seq analysis of the liver in G2019S LRRK2 knockin mice</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet-38">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet-38" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Bulk RNA-seq analysis of the liver in G2019S LRRK2 knockin mice</h3>
          <p><strong>Dataset ID:</strong> <code>lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet</code></p>
          <p><strong>Description:</strong> The liver was collected from G2019S LRRK2 knockin mice and their wild-type littermates (3-5 months old) for bulk RNA-seq analysis. Each experimental group contained biological replicates (n = 4 per group).</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.1</p>
          <p><strong>Latest CDE version:</strong> v4.1</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18273808" target="_blank" rel="noopener">10.5281/zenodo.18273808</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">mouse</span> <span class="tag-pill">sn-rnaseq</span></p>
          <p><strong>Keywords:</strong> mouse, sn-rnaseq, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.1</td>
                <td>v1.0</td>
                <td>v4.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-mouse-sn-rnaseq-midbrain-g2019s-hf-diet</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-pmdbs-bulk-rnaseq-mfg-39" data-search="lee-pmdbs-bulk-rnaseq-mfg bulk rna-sequencing of human middle frontal gyrus bulk rna-seq data from middle frontal gyrus samples of human pd and control postmortem brains. pmdbs-bulk-rnaseq cc-by-4.0 10.5281/zenodo.16748937 lee pmdbs-bulk-rnaseq pmdbs-bulk-rnaseq pmdbs-bulk-rnaseq lee gs://asap-raw-team-lee-pmdbs-bulk-rnaseq-mfg gs://asap-dev-team-lee-pmdbs-bulk-rnaseq-mfg gs://asap-uat-team-lee-pmdbs-bulk-rnaseq-mfg gs://asap-curated-team-lee-pmdbs-bulk-rnaseq-mfg v2.0.0 v3.0.0 v4.0.0 v4.1.0 v2.0.0 v1.0 v3.0 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3 v4.1.0 v1.1 v3.3" data-tags="lee||pmdbs-bulk-rnaseq">
      <td><code>lee-pmdbs-bulk-rnaseq-mfg</code></td>
      <td>Bulk RNA-sequencing of human middle frontal gyrus</td>
      <td>pmdbs-bulk-rnaseq</td>
      <td>v1.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-pmdbs-bulk-rnaseq-mfg-39">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-pmdbs-bulk-rnaseq-mfg-39" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Bulk RNA-sequencing of human middle frontal gyrus</h3>
          <p><strong>Dataset ID:</strong> <code>lee-pmdbs-bulk-rnaseq-mfg</code></p>
          <p><strong>Description:</strong> Bulk RNA-seq data from middle frontal gyrus samples of human PD and control postmortem brains.</p>
          <p><strong>Collection:</strong> pmdbs-bulk-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16748937" target="_blank" rel="noopener">10.5281/zenodo.16748937</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">pmdbs-bulk-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs-bulk-rnaseq, pmdbs-bulk-rnaseq, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v1.0</td>
                <td>v3.0</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-pmdbs-bulk-rnaseq-mfg</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-pmdbs-bulk-rnaseq-mfg</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-pmdbs-bulk-rnaseq-mfg</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-pmdbs-bulk-rnaseq-mfg</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-lee-pmdbs-sn-rnaseq-40" data-search="lee-pmdbs-sn-rnaseq single nucleus rna-sequencing of human postmortem hippocampus, middle frontal gyrus, and substantia nigra single nucleus rna-seq data from hippocampus, middle frontal gyrus, and substantia nigra samples of human pd and control postmortem brains. all three brain regions were co-sampled from each donor to enable direct comparison of transcriptomic signatures across anatomically and functionally distinct regions within the same brain. pmdbs-sc-rnaseq cc-by-4.0 10.5281/zenodo.16744323 lee pmdbs-sc-rnaseq pmdbs-sc-rnaseq pmdbs-sc-rnaseq lee gs://asap-raw-team-lee-pmdbs-sn-rnaseq gs://asap-dev-team-lee-pmdbs-sn-rnaseq gs://asap-uat-team-lee-pmdbs-sn-rnaseq gs://asap-curated-team-lee-pmdbs-sn-rnaseq v1.0.0 v2.0.0 v3.0.0 v4.0.0 v4.1.0 v1.0.0 v1.0 v2.1 v2.0.0 v1.0 v3.0 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3 v4.1.0 v1.1 v3.3" data-tags="lee||pmdbs-sc-rnaseq">
      <td><code>lee-pmdbs-sn-rnaseq</code></td>
      <td>Single nucleus RNA-sequencing of human postmortem hippocampus, middle frontal gyrus, and substantia nigra</td>
      <td>pmdbs-sc-rnaseq</td>
      <td>v1.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-lee-pmdbs-sn-rnaseq-40">View</button></td>
    </tr>
    <tr id="dataset-detail-lee-pmdbs-sn-rnaseq-40" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single nucleus RNA-sequencing of human postmortem hippocampus, middle frontal gyrus, and substantia nigra</h3>
          <p><strong>Dataset ID:</strong> <code>lee-pmdbs-sn-rnaseq</code></p>
          <p><strong>Description:</strong> Single nucleus RNA-seq data from hippocampus, middle frontal gyrus, and substantia nigra samples of human PD and control postmortem brains. All three brain regions were co-sampled from each donor to enable direct comparison of transcriptomic signatures across anatomically and functionally distinct regions within the same brain.</p>
          <p><strong>Collection:</strong> pmdbs-sc-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16744323" target="_blank" rel="noopener">10.5281/zenodo.16744323</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lee</span> <span class="tag-pill">pmdbs-sc-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs-sc-rnaseq, pmdbs-sc-rnaseq, lee</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v1.0</td>
                <td>v3.0</td>
              </tr>
              <tr>
                <td>v1.0.0</td>
                <td>v1.0</td>
                <td>v2.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-lee-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-lee-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-lee-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-lee-pmdbs-sn-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-liddle-human-colon-spatial-cosmx-protein-64p-41" data-search="liddle-human-colon-spatial-cosmx-protein-64p bolen human sigmoid colon rna cosmx dataset nanostring cosmxtm human sigmoid colon rna 1000-plex dataset exported from atomx for downstream analysis spatially resolves up to 1000 transcripts (cmx hs univ cell panel rna kit ea: cat# 121500002). a custom spike in for the following 12 genes labeled following the hugo gene nomenclature were included in the rna assay: slc6a4 (solute carrier family 6 member 4), chga (chromogranin a), slc11a2 (solute carrier family 11 member 2), fth1(ferritin heavy chain 1), hamp (hepcidin antimicrobial peptide), ireb2 (iron responsive element binding protein 2), itpkb (inositol-trisphosphate 3-kinase b), ndufb1 (nadh: ubiquinone oxidoreductase subunit b1), pink1 (pten-induced kinase 1), pyy (peptide yy), rab8a (rab8a, member ras oncogene family), tf (transferrin). we used morphology markers cd45, panck, cd3 to visualize the tissue and picked two 0.5mm fields of view (fov) per sample. na cc-by-4.0 10.5281/zenodo.17917771 human-colon liddle spatial-cosmx human-colon spatial-cosmx liddle gs://asap-raw-team-liddle-human-colon-spatial-cosmx-protein-64p gs://asap-dev-team-liddle-human-colon-spatial-cosmx-protein-64p gs://asap-uat-team-liddle-human-colon-spatial-cosmx-protein-64p gs://asap-curated-team-liddle-human-colon-spatial-cosmx-protein-64p v4.0.1 v4.0.1 v1.0 v4.1" data-tags="human-colon||liddle||spatial-cosmx">
      <td><code>liddle-human-colon-spatial-cosmx-protein-64p</code></td>
      <td>Bolen Human Sigmoid Colon RNA CosMx Dataset</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-liddle-human-colon-spatial-cosmx-protein-64p-41">View</button></td>
    </tr>
    <tr id="dataset-detail-liddle-human-colon-spatial-cosmx-protein-64p-41" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Bolen Human Sigmoid Colon RNA CosMx Dataset</h3>
          <p><strong>Dataset ID:</strong> <code>liddle-human-colon-spatial-cosmx-protein-64p</code></p>
          <p><strong>Description:</strong> NanoString CosMxTM human sigmoid colon RNA 1000-plex dataset exported from Atomx for downstream analysis spatially resolves up to 1000 transcripts (CMx Hs Univ Cell Panel RNA Kit EA: CAT# 121500002). A custom spike in for the following 12 genes labeled following the HUGO gene nomenclature were included in the RNA assay: SLC6A4 (solute carrier family 6 member 4), CHGA (chromogranin A), SLC11A2 (solute carrier family 11 member 2), FTH1(ferritin heavy chain 1), HAMP (hepcidin antimicrobial peptide), IREB2 (iron responsive element binding protein 2), ITPKB (Inositol-Trisphosphate 3-Kinase B), NDUFB1 (NADH: Ubiquinone Oxidoreductase Subunit B1), PINK1 (PTEN-induced kinase 1), PYY (peptide YY), RAB8A (RAB8A, member RAS oncogene family), TF (transferrin). We used morphology markers CD45, PanCK, CD3 to visualize the tissue and picked two 0.5mm fields of view (FOV) per sample.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.1</p>
          <p><strong>Latest CDE version:</strong> v4.1</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17917771" target="_blank" rel="noopener">10.5281/zenodo.17917771</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">human-colon</span> <span class="tag-pill">liddle</span> <span class="tag-pill">spatial-cosmx</span></p>
          <p><strong>Keywords:</strong> human-colon, spatial-cosmx, liddle</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.1</td>
                <td>v1.0</td>
                <td>v4.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-liddle-human-colon-spatial-cosmx-protein-64p</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-liddle-human-colon-spatial-cosmx-protein-64p</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-liddle-human-colon-spatial-cosmx-protein-64p</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-liddle-human-colon-spatial-cosmx-protein-64p</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-liddle-human-colon-spatial-cosmx-rna-1000p-42" data-search="liddle-human-colon-spatial-cosmx-rna-1000p bolen human sigmoid colon rna cosmx dataset nanostring cosmxtm human sigmoid colon rna 1000-plex dataset exported from atomx for downstream analysis spatially resolves up to 1000 transcripts (cmx hs univ cell panel rna kit ea: cat# 121500002). a custom spike in for the following 12 genes labeled following the hugo gene nomenclature were included in the rna assay: slc6a4 (solute carrier family 6 member 4), chga (chromogranin a), slc11a2 (solute carrier family 11 member 2), fth1(ferritin heavy chain 1), hamp (hepcidin antimicrobial peptide), ireb2 (iron responsive element binding protein 2), itpkb (inositol-trisphosphate 3-kinase b), ndufb1 (nadh: ubiquinone oxidoreductase subunit b1), pink1 (pten-induced kinase 1), pyy (peptide yy), rab8a (rab8a, member ras oncogene family), tf (transferrin). we used morphology markers cd45, panck, cd3 to visualize the tissue and picked two 0.5mm fields of view (fov) per sample. na cc-by-4.0 10.5281/zenodo.17917788 human-colon liddle spatial-cosmx human-colon spatial-cosmx liddle gs://asap-raw-team-liddle-human-colon-spatial-cosmx-rna-1000p gs://asap-dev-team-liddle-human-colon-spatial-cosmx-rna-1000p gs://asap-uat-team-liddle-human-colon-spatial-cosmx-rna-1000p gs://asap-curated-team-liddle-human-colon-spatial-cosmx-rna-1000p v4.0.1 v4.0.1 v1.0 v4.1" data-tags="human-colon||liddle||spatial-cosmx">
      <td><code>liddle-human-colon-spatial-cosmx-rna-1000p</code></td>
      <td>Bolen Human Sigmoid Colon RNA CosMx Dataset</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-liddle-human-colon-spatial-cosmx-rna-1000p-42">View</button></td>
    </tr>
    <tr id="dataset-detail-liddle-human-colon-spatial-cosmx-rna-1000p-42" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Bolen Human Sigmoid Colon RNA CosMx Dataset</h3>
          <p><strong>Dataset ID:</strong> <code>liddle-human-colon-spatial-cosmx-rna-1000p</code></p>
          <p><strong>Description:</strong> NanoString CosMxTM human sigmoid colon RNA 1000-plex dataset exported from Atomx for downstream analysis spatially resolves up to 1000 transcripts (CMx Hs Univ Cell Panel RNA Kit EA: CAT# 121500002). A custom spike in for the following 12 genes labeled following the HUGO gene nomenclature were included in the RNA assay: SLC6A4 (solute carrier family 6 member 4), CHGA (chromogranin A), SLC11A2 (solute carrier family 11 member 2), FTH1(ferritin heavy chain 1), HAMP (hepcidin antimicrobial peptide), IREB2 (iron responsive element binding protein 2), ITPKB (Inositol-Trisphosphate 3-Kinase B), NDUFB1 (NADH: Ubiquinone Oxidoreductase Subunit B1), PINK1 (PTEN-induced kinase 1), PYY (peptide YY), RAB8A (RAB8A, member RAS oncogene family), TF (transferrin). We used morphology markers CD45, PanCK, CD3 to visualize the tissue and picked two 0.5mm fields of view (FOV) per sample.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.1</p>
          <p><strong>Latest CDE version:</strong> v4.1</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17917788" target="_blank" rel="noopener">10.5281/zenodo.17917788</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">human-colon</span> <span class="tag-pill">liddle</span> <span class="tag-pill">spatial-cosmx</span></p>
          <p><strong>Keywords:</strong> human-colon, spatial-cosmx, liddle</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.1</td>
                <td>v1.0</td>
                <td>v4.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-liddle-human-colon-spatial-cosmx-rna-1000p</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-liddle-human-colon-spatial-cosmx-rna-1000p</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-liddle-human-colon-spatial-cosmx-rna-1000p</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-liddle-human-colon-spatial-cosmx-rna-1000p</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-metadata-43" data-search="metadata single-cell rnaseq of human pbmcs from healthy control, rbd, and pd. we performed 10x genomics single-cell rnasequencing of human prepheral blood mononuclear cells from healthy control, pd and rbd patients. this dataset contains raw fastq files. sequencing was performed using novaseq 6000 s4 pe 100bp. reads were processed using the 10x genomics cell ranger single cell 2.0.0 pipeline. fastqs generated from sequencing output were aligned to the human grch38 reference genome using star algorithm 2.7.3a. na {&#x27;id&#x27;: &#x27;cc-by-4.0&#x27;}      " data-tags="">
      <td><code>metadata</code></td>
      <td>Single-cell RNAseq of human PBMCs from healthy control, RBD, and PD.</td>
      <td>NA</td>
      <td>TBD</td>
      <td>TBD</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-metadata-43">View</button></td>
    </tr>
    <tr id="dataset-detail-metadata-43" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single-cell RNAseq of human PBMCs from healthy control, RBD, and PD.</h3>
          <p><strong>Dataset ID:</strong> <code>metadata</code></p>
          <p><strong>Description:</strong> We performed 10X Genomics single-cell RNAsequencing of human prepheral blood mononuclear cells from healthy control, PD and RBD patients. This dataset contains raw FASTQ files. Sequencing was performed using NovaSeq 6000 S4 PE 100bp. Reads were processed using the 10X Genomics Cell Ranger Single Cell 2.0.0 pipeline. FASTQs generated from sequencing output were aligned to the human GRCh38 reference genome using STAR algorithm 2.7.3a.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> TBD</p>
          <p><strong>Latest release:</strong> TBD</p>
          <p><strong>Latest CDE version:</strong> TBD</p>
          <p><strong>License:</strong> {&#x27;id&#x27;: &#x27;cc-by-4.0&#x27;}</p>
          <p><strong>DOI:</strong> TBD</p>
          <p><strong>Tags:</strong> NA</p>
          <p><strong>Keywords:</strong> TBD</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td colspan="3">No release history listed.</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td colspan="2">No bucket paths listed.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-schapira-fecal-metagenome-human-baseline-44" data-search="schapira-fecal-metagenome-human-baseline human fecal shotgun metagenomic sequencing in parkinson&#x27;s disease individuals, non-manifesting gba1 variant carriers and healthy controls the microbial species abundance table: list of microbial species detected from fecal samples sequenced by shotgun metagenomic sequencing. software used: meteor, in combination with human digestive (gut and oral) microbial species catalogues. the species are listed as msp_id, which corresponds to metagenomic species pangenomes (msps), which is a collection of known or still unknown species reconstructed from human gut metagenomic assemblies. the msps are annotated at all taxonomical level using the genome taxonomy database gdtb r07-rs207 database, up until the lowest known taxonomical rank. the microbial functional abundance table: list of microbial functions detected from fecal samples sequenced by shotgun metagenomic sequencing. software used: meteor, in combination with human digestive (gut and oral) microbial gene catalogues and annotated with kegg, eggnog and tigrfam databases. these databases are used to infer the presence, abundance and completeness of functional modules (gut-brain modules, gut-metabolic modules and kegg modules) in each metagenomic samples. na cc-by-4.0 10.5281/zenodo.18353680 fecal-metagenome schapira fecal-metagenome schapira gs://asap-raw-team-schapira-fecal-metagenome-human-baseline gs://asap-dev-team-schapira-fecal-metagenome-human-baseline gs://asap-uat-team-schapira-fecal-metagenome-human-baseline gs://asap-curated-team-schapira-fecal-metagenome-human-baseline v4.0.1 v4.0.1 v1.0 v4.1" data-tags="fecal-metagenome||schapira">
      <td><code>schapira-fecal-metagenome-human-baseline</code></td>
      <td>Human fecal shotgun metagenomic sequencing in Parkinson&#x27;s disease individuals, non-manifesting GBA1 variant carriers and healthy controls</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-schapira-fecal-metagenome-human-baseline-44">View</button></td>
    </tr>
    <tr id="dataset-detail-schapira-fecal-metagenome-human-baseline-44" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Human fecal shotgun metagenomic sequencing in Parkinson&#x27;s disease individuals, non-manifesting GBA1 variant carriers and healthy controls</h3>
          <p><strong>Dataset ID:</strong> <code>schapira-fecal-metagenome-human-baseline</code></p>
          <p><strong>Description:</strong> The microbial species abundance table: list of microbial species detected from fecal samples sequenced by shotgun metagenomic sequencing. Software used: METEOR, in combination with human digestive (gut and oral) microbial species catalogues. The species are listed as msp_ID, which corresponds to metagenomic species pangenomes (MSPs), which is a collection of known or still unknown species reconstructed from human gut metagenomic assemblies. The MSPs are annotated at all taxonomical level using the Genome Taxonomy Database GDTB R07-RS207 database, up until the lowest known taxonomical rank. The microbial functional abundance table: list of microbial functions detected from fecal samples sequenced by shotgun metagenomic sequencing. Software used: METEOR, in combination with human digestive (gut and oral) microbial gene catalogues and annotated with KEGG, eggNOG and TIGRFAM databases. These databases are used to infer the presence, abundance and completeness of functional modules (Gut-Brain modules, Gut-Metabolic modules and KEGG modules) in each metagenomic samples.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.1</p>
          <p><strong>Latest CDE version:</strong> v4.1</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18353680" target="_blank" rel="noopener">10.5281/zenodo.18353680</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">fecal-metagenome</span> <span class="tag-pill">schapira</span></p>
          <p><strong>Keywords:</strong> fecal-metagenome, schapira</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.1</td>
                <td>v1.0</td>
                <td>v4.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-schapira-fecal-metagenome-human-baseline</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-schapira-fecal-metagenome-human-baseline</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-schapira-fecal-metagenome-human-baseline</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-schapira-fecal-metagenome-human-baseline</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-scherzer-pmdbs-genetics-45" data-search="scherzer-pmdbs-genetics pd5d_mtg_mega_chip_genotype this dataset represents the plink bed format genotype data of pd5d  subjects (pd5d_mtg_snrnaseq). all subjects were genotyped on the  infinium multi-ethnic global-8 v1 chip. raw genotypes were processed  with plink (v1.90) and basic quality control, including removal of low quality genotypes and low-quality variants, was performed. please note  that the position information in the file was based on human grc37/hg19  reference genome. na cc-by-4.0 10.5281/zenodo.17242295 other-pmdbs pmdbs-genetics scherzer pmdbs-genetics other-pmdbs scherzer gs://asap-raw-team-scherzer-pmdbs-genetics gs://asap-dev-team-scherzer-pmdbs-genetics gs://asap-uat-team-scherzer-pmdbs-genetics gs://asap-curated-team-scherzer-pmdbs-genetics v3.0.1 v4.0.0 v4.1.0 v3.0.1 v1.0 v3.3 v4.0.0 v1.0 v3.3 v4.1.0 v1.1 v3.3" data-tags="other-pmdbs||pmdbs-genetics||scherzer">
      <td><code>scherzer-pmdbs-genetics</code></td>
      <td>PD5D_MTG_MEGA_Chip_Genotype</td>
      <td>NA</td>
      <td>v1.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-scherzer-pmdbs-genetics-45">View</button></td>
    </tr>
    <tr id="dataset-detail-scherzer-pmdbs-genetics-45" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>PD5D_MTG_MEGA_Chip_Genotype</h3>
          <p><strong>Dataset ID:</strong> <code>scherzer-pmdbs-genetics</code></p>
          <p><strong>Description:</strong> This dataset represents the PLINK bed format genotype data of PD5D  subjects (PD5D_MTG_snRNAseq). All subjects were genotyped on the  Infinium Multi-Ethnic Global-8 v1 chip. Raw genotypes were processed  with PLINK (v1.90) and basic quality control, including removal of low quality genotypes and low-quality variants, was performed. Please note  that the position information in the file was based on human GRC37/hg19  reference genome.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17242295" target="_blank" rel="noopener">10.5281/zenodo.17242295</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">other-pmdbs</span> <span class="tag-pill">pmdbs-genetics</span> <span class="tag-pill">scherzer</span></p>
          <p><strong>Keywords:</strong> pmdbs-genetics, other-pmdbs, scherzer</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.1</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-scherzer-pmdbs-genetics</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-scherzer-pmdbs-genetics</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-scherzer-pmdbs-genetics</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-scherzer-pmdbs-genetics</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-scherzer-pmdbs-lr-wgs-46" data-search="scherzer-pmdbs-lr-wgs pd5d long read dna-seq this dataset contains ccs corrected hifi long-read dna sequencing (lrdnaseq) in fastq format for 100 pmdbs samples from parkinson&#x27;s patients and healthy controls. it&#x27;s part of the pd5d atlas, where the same subjects were also profiled with other omics assays including genotyping, single-cell atacseq, and spatial transcriptomics. na cc-by-4.0 10.5281/zenodo.19124632 lr-wgs pmdbs scherzer pmdbs lr-wgs scherzer gs://asap-raw-team-scherzer-pmdbs-lr-wgs gs://asap-dev-team-scherzer-pmdbs-lr-wgs gs://asap-uat-team-scherzer-pmdbs-lr-wgs gs://asap-curated-team-scherzer-pmdbs-lr-wgs v4.1.1 v4.1.1 v1.0 v4.4" data-tags="lr-wgs||pmdbs||scherzer">
      <td><code>scherzer-pmdbs-lr-wgs</code></td>
      <td>PD5D long read DNA-seq</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-scherzer-pmdbs-lr-wgs-46">View</button></td>
    </tr>
    <tr id="dataset-detail-scherzer-pmdbs-lr-wgs-46" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>PD5D long read DNA-seq</h3>
          <p><strong>Dataset ID:</strong> <code>scherzer-pmdbs-lr-wgs</code></p>
          <p><strong>Description:</strong> This dataset contains CCS corrected HiFi long-read DNA sequencing (lrDNAseq) in FASTQ format for 100 PMDBS samples from Parkinson&#x27;s patients and healthy controls. It&#x27;s part of the PD5D atlas, where the same subjects were also profiled with other omics assays including genotyping, single-cell ATACseq, and spatial transcriptomics.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.1</p>
          <p><strong>Latest CDE version:</strong> v4.4</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.19124632" target="_blank" rel="noopener">10.5281/zenodo.19124632</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">lr-wgs</span> <span class="tag-pill">pmdbs</span> <span class="tag-pill">scherzer</span></p>
          <p><strong>Keywords:</strong> pmdbs, lr-wgs, scherzer</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.1</td>
                <td>v1.0</td>
                <td>v4.4</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-scherzer-pmdbs-lr-wgs</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-scherzer-pmdbs-lr-wgs</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-scherzer-pmdbs-lr-wgs</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-scherzer-pmdbs-lr-wgs</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel-47" data-search="scherzer-pmdbs-sn-rnaseq-midbrain-hybsel pd5d midbrain single-nucleus rna-seq hybrid selection this dataset contains raw fastq files from the midbrain single-nucleus rna sequencing (snrnaseq) dataset with hybrid selection for the matching pmdbs samples from the pd5d chort. the same subjects were also profiled with other omics assays including genomic dnaseq, genotyping, single-cell atacseq, and spatial transcriptomics. na cc-by-4.0 10.5281/zenodo.19124469 pmdbs scherzer sn-rnaseq pmdbs sn-rnaseq scherzer gs://asap-raw-team-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel gs://asap-dev-team-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel gs://asap-uat-team-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel gs://asap-curated-team-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel v4.1.1 v4.1.1 v1.0 v4.4" data-tags="pmdbs||scherzer||sn-rnaseq">
      <td><code>scherzer-pmdbs-sn-rnaseq-midbrain-hybsel</code></td>
      <td>PD5D midbrain single-nucleus RNA-seq hybrid selection</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel-47">View</button></td>
    </tr>
    <tr id="dataset-detail-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel-47" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>PD5D midbrain single-nucleus RNA-seq hybrid selection</h3>
          <p><strong>Dataset ID:</strong> <code>scherzer-pmdbs-sn-rnaseq-midbrain-hybsel</code></p>
          <p><strong>Description:</strong> This dataset contains raw FASTQ files from the midbrain single-nucleus RNA sequencing (snRNAseq) dataset with hybrid selection for the matching PMDBS samples from the PD5D chort. The same subjects were also profiled with other omics assays including genomic DNAseq, genotyping, single-cell ATACseq, and spatial transcriptomics.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.1</p>
          <p><strong>Latest CDE version:</strong> v4.4</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.19124469" target="_blank" rel="noopener">10.5281/zenodo.19124469</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs</span> <span class="tag-pill">scherzer</span> <span class="tag-pill">sn-rnaseq</span></p>
          <p><strong>Keywords:</strong> pmdbs, sn-rnaseq, scherzer</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.1</td>
                <td>v1.0</td>
                <td>v4.4</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-scherzer-pmdbs-sn-rnaseq-midbrain-hybsel</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-scherzer-pmdbs-sn-rnaseq-mtg-48" data-search="scherzer-pmdbs-sn-rnaseq-mtg pd5d_mtg_snrnaseq this dataset contains single-nucleus rna sequencing (snrnaseq) raw data in  fastq format for 94 human middle temporal gyrus (mtg) samples from  parkinson&#x27;s patients and healthy controls. it&#x27;s part of the pd5d atlas, where  the same subjects were also profiled with other omics assays incl. genotyping,  single-cell atacseq, and spatial transcriptomics.

version bump from 1.1 to 1.2

the updated datasets fix inconsistencies in the asap assigned `asap_subject_id` and `asap_sample_id` for these previously released pmdbs datasets. these erroneously included the string &quot;pmbds&quot;, now replaced with &quot;pmdbs&quot;. this change does not affect the underlying data files, but does update the metadata to be consistent with the naming convention used for all other pmdbs datasets and the corresponding cdes. pmdbs-sc-rnaseq cc-by-4.0 10.5281/zenodo.16751625 pmdbs-sc-rnaseq scherzer pmdbs-sc-rnaseq pmdbs-sc-rnaseq scherzer gs://asap-raw-team-scherzer-pmdbs-sn-rnaseq-mtg gs://asap-dev-team-scherzer-pmdbs-sn-rnaseq-mtg gs://asap-uat-team-scherzer-pmdbs-sn-rnaseq-mtg gs://asap-curated-team-scherzer-pmdbs-sn-rnaseq-mtg v1.0.0 v2.0.0 v3.0.0 v3.0.1 v4.0.0 v4.1.0 v1.0.0 v1.0 v2.1 v2.0.0 v1.0 v3.0 v3.0.0 v1.0 v3.2 v3.0.1 v1.1 v3.3 v4.0.0 v1.1 v3.3 v4.1.0 v1.2 v3.3" data-tags="pmdbs-sc-rnaseq||scherzer">
      <td><code>scherzer-pmdbs-sn-rnaseq-mtg</code></td>
      <td>PD5D_MTG_snRNAseq</td>
      <td>pmdbs-sc-rnaseq</td>
      <td>v1.2</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-scherzer-pmdbs-sn-rnaseq-mtg-48">View</button></td>
    </tr>
    <tr id="dataset-detail-scherzer-pmdbs-sn-rnaseq-mtg-48" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>PD5D_MTG_snRNAseq</h3>
          <p><strong>Dataset ID:</strong> <code>scherzer-pmdbs-sn-rnaseq-mtg</code></p>
          <p><strong>Description:</strong> This dataset contains single-nucleus RNA sequencing (snRNAseq) raw data in  FASTQ format for 94 human middle temporal gyrus (MTG) samples from  Parkinson&#x27;s patients and healthy controls. It&#x27;s part of the PD5D atlas, where  the same subjects were also profiled with other omics assays incl. genotyping,  single-cell ATACseq, and spatial transcriptomics.

Version bump from 1.1 to 1.2

The updated Datasets fix inconsistencies in the ASAP assigned `ASAP_subject_id` and `ASAP_sample_id` for these previously released PMDBS Datasets. These erroneously included the string &quot;PMBDS&quot;, now replaced with &quot;PMDBS&quot;. This change does not affect the underlying data files, but does update the metadata to be consistent with the naming convention used for all other PMDBS Datasets and the corresponding CDEs.</p>
          <p><strong>Collection:</strong> pmdbs-sc-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.2</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16751625" target="_blank" rel="noopener">10.5281/zenodo.16751625</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs-sc-rnaseq</span> <span class="tag-pill">scherzer</span></p>
          <p><strong>Keywords:</strong> pmdbs-sc-rnaseq, pmdbs-sc-rnaseq, scherzer</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.2</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.1</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v1.0</td>
                <td>v3.0</td>
              </tr>
              <tr>
                <td>v1.0.0</td>
                <td>v1.0</td>
                <td>v2.1</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-scherzer-pmdbs-sn-rnaseq-mtg</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-scherzer-pmdbs-sn-rnaseq-mtg</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-scherzer-pmdbs-sn-rnaseq-mtg</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-scherzer-pmdbs-sn-rnaseq-mtg</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-scherzer-pmdbs-sn-rnaseq-mtg-hybsel-49" data-search="scherzer-pmdbs-sn-rnaseq-mtg-hybsel pd5d_mtg_snrnaseq_hybsel this dataset contains the raw data in fastq format for single-nucleus rna  sequencing (snrnaseq) enriched with agilent sureselect for reads from a list  of targeted transcripts for human middle temporal gyrus (mtg) samples from  parkinson&#x27;s patients and healthy controls. this data comes from the same 10x  libraries as pd5d_mtg_snrnaseq, except with the additional enrichment  step before sequencing. it&#x27;s part of the pd5d cohort, where the same subjects  were also profiled with other omics assays incl. genotyping, single-cell  atacseq, and spatial transcriptomics.

version bump from 1.1 to 1.2

the updated datasets fix inconsistencies in the asap assigned `asap_subject_id` and `asap_sample_id` for these previously released pmdbs datasets. these erroneously included the string &quot;pmbds&quot;, now replaced with &quot;pmdbs&quot;. this change does not affect the underlying data files, but does update the metadata to be consistent with the naming convention used for all other pmdbs datasets and the corresponding cdes. na cc-by-4.0 10.5281/zenodo.16885839 other-pmdbs pmdbs-other scherzer pmdbs-other other-pmdbs scherzer gs://asap-raw-team-scherzer-pmdbs-sn-rnaseq-mtg-hybsel gs://asap-dev-team-scherzer-pmdbs-sn-rnaseq-mtg-hybsel gs://asap-uat-team-scherzer-pmdbs-sn-rnaseq-mtg-hybsel gs://asap-curated-team-scherzer-pmdbs-sn-rnaseq-mtg-hybsel v2.0.0 v3.0.0 v3.0.1 v4.0.0 v4.1.0 v2.0.0 v1.0 v3.0 v3.0.0 v1.0 v3.2 v3.0.1 v1.1 v3.3 v4.0.0 v1.1 v3.3 v4.1.0 v1.2 v3.3" data-tags="other-pmdbs||pmdbs-other||scherzer">
      <td><code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
      <td>PD5D_MTG_snRNAseq_hybsel</td>
      <td>NA</td>
      <td>v1.2</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-scherzer-pmdbs-sn-rnaseq-mtg-hybsel-49">View</button></td>
    </tr>
    <tr id="dataset-detail-scherzer-pmdbs-sn-rnaseq-mtg-hybsel-49" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>PD5D_MTG_snRNAseq_hybsel</h3>
          <p><strong>Dataset ID:</strong> <code>scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></p>
          <p><strong>Description:</strong> This dataset contains the raw data in FASTQ format for single-nucleus RNA  sequencing (snRNAseq) enriched with Agilent SureSelect for reads from a list  of targeted transcripts for human middle temporal gyrus (MTG) samples from  Parkinson&#x27;s patients and healthy controls. This data comes from the same 10X  libraries as PD5D_MTG_snRNAseq, except with the additional enrichment  step before sequencing. It&#x27;s part of the PD5D cohort, where the same subjects  were also profiled with other omics assays incl. genotyping, single-cell  ATACseq, and spatial transcriptomics.

Version bump from 1.1 to 1.2

The updated Datasets fix inconsistencies in the ASAP assigned `ASAP_subject_id` and `ASAP_sample_id` for these previously released PMDBS Datasets. These erroneously included the string &quot;PMBDS&quot;, now replaced with &quot;PMDBS&quot;. This change does not affect the underlying data files, but does update the metadata to be consistent with the naming convention used for all other PMDBS Datasets and the corresponding CDEs.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.2</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16885839" target="_blank" rel="noopener">10.5281/zenodo.16885839</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">other-pmdbs</span> <span class="tag-pill">pmdbs-other</span> <span class="tag-pill">scherzer</span></p>
          <p><strong>Keywords:</strong> pmdbs-other, other-pmdbs, scherzer</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.2</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.1</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v1.0</td>
                <td>v3.0</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-scherzer-pmdbs-sn-rnaseq-mtg-hybsel</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-scherzer-pmdbs-spatial-visium-mtg-50" data-search="scherzer-pmdbs-spatial-visium-mtg pd5d_mtg_visium10x_st visium 10x spatial transcriptomic raw data in fastq format of the middle  temporal gyrus of 96 human subjects. individuals with incidental lewy body  disease, clinical pd, and healthy control were included. in addition to subject level metadata, visium spatial metadata such as h&amp;e images and spot  coordinates are included.   these data are one component of the pd5d cohort, which intends to build a  multi-dimensional and multi-omic atlas of pd pathology. for the same subjects, other omics assays have been collected including genotyping,  snrna-seq, and scatac-seq across two brain tissues: middle temporal gyrus  and substantia nigra. pmdbs-spatial-rnaseq cc-by-4.0 10.5281/zenodo.17242087 other-pmdbs pmdbs-spatial-rnaseq scherzer pmdbs-spatial-rnaseq other-pmdbs scherzer gs://asap-raw-team-scherzer-pmdbs-spatial-visium-mtg gs://asap-dev-team-scherzer-pmdbs-spatial-visium-mtg gs://asap-uat-team-scherzer-pmdbs-spatial-visium-mtg gs://asap-curated-team-scherzer-pmdbs-spatial-visium-mtg v3.0.1 v4.0.0 v4.1.0 v3.0.1 v1.0 v3.3 v4.0.0 v1.0 v3.3 v4.1.0 v1.1 v3.3" data-tags="other-pmdbs||pmdbs-spatial-rnaseq||scherzer">
      <td><code>scherzer-pmdbs-spatial-visium-mtg</code></td>
      <td>PD5D_MTG_Visium10x_ST</td>
      <td>pmdbs-spatial-rnaseq</td>
      <td>v1.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-scherzer-pmdbs-spatial-visium-mtg-50">View</button></td>
    </tr>
    <tr id="dataset-detail-scherzer-pmdbs-spatial-visium-mtg-50" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>PD5D_MTG_Visium10x_ST</h3>
          <p><strong>Dataset ID:</strong> <code>scherzer-pmdbs-spatial-visium-mtg</code></p>
          <p><strong>Description:</strong> Visium 10x spatial transcriptomic raw data in FASTQ format of the middle  temporal gyrus of 96 human subjects. Individuals with incidental Lewy body  disease, clinical PD, and healthy control were included. In addition to subject level metadata, Visium spatial metadata such as H&amp;E images and spot  coordinates are included.   These data are one component of the PD5D cohort, which intends to build a  multi-dimensional and multi-omic atlas of PD pathology. For the same subjects, other omics assays have been collected including genotyping,  snRNA-seq, and scATAC-seq across two brain tissues: middle temporal gyrus  and substantia nigra.</p>
          <p><strong>Collection:</strong> pmdbs-spatial-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17242087" target="_blank" rel="noopener">10.5281/zenodo.17242087</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">other-pmdbs</span> <span class="tag-pill">pmdbs-spatial-rnaseq</span> <span class="tag-pill">scherzer</span></p>
          <p><strong>Keywords:</strong> pmdbs-spatial-rnaseq, other-pmdbs, scherzer</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.1</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-scherzer-pmdbs-spatial-visium-mtg</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-scherzer-pmdbs-spatial-visium-mtg</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-scherzer-pmdbs-spatial-visium-mtg</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-scherzer-pmdbs-spatial-visium-mtg</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-schlossmacher-mouse-sn-rnaseq-osn-aav-transd-51" data-search="schlossmacher-mouse-sn-rnaseq-osn-aav-transd snrnaseq of olfactory epithelium with aav serotypes for transduction of olfactory sensory neurons in mus musculus single-nucleus rna sequencing data of 4 mice, each inoculated with 4 aav serotypes. the mice were all male and 8-10 weeks of age at when olfactory epithelium tissue was harvested. samples were paired-end sequences using v3.1 – dual index using illumina novaseq 6000 sequencer. na cc-by-4.0 10.5281/zenodo.17358327 mouse-sc-rnaseq other-mouse schlossmacher mouse-sc-rnaseq other-mouse schlossmacher gs://asap-raw-team-schlossmacher-mouse-sn-rnaseq-osn-aav-transd gs://asap-dev-team-schlossmacher-mouse-sn-rnaseq-osn-aav-transd gs://asap-uat-team-schlossmacher-mouse-sn-rnaseq-osn-aav-transd gs://asap-curated-team-schlossmacher-mouse-sn-rnaseq-osn-aav-transd v3.0.1 v4.0.0 v3.0.1 v1.0 v3.3 v4.0.0 v1.0 v3.3" data-tags="mouse-sc-rnaseq||other-mouse||schlossmacher">
      <td><code>schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
      <td>snRNAseq of olfactory epithelium with AAV serotypes for transduction of olfactory sensory neurons in Mus musculus</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-schlossmacher-mouse-sn-rnaseq-osn-aav-transd-51">View</button></td>
    </tr>
    <tr id="dataset-detail-schlossmacher-mouse-sn-rnaseq-osn-aav-transd-51" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>snRNAseq of olfactory epithelium with AAV serotypes for transduction of olfactory sensory neurons in Mus musculus</h3>
          <p><strong>Dataset ID:</strong> <code>schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></p>
          <p><strong>Description:</strong> Single-nucleus RNA sequencing data of 4 mice, each inoculated with 4 AAV serotypes. The mice were all male and 8-10 weeks of age at when olfactory epithelium tissue was harvested. Samples were paired-end sequences using v3.1 – Dual Index using Illumina Novaseq 6000 sequencer.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17358327" target="_blank" rel="noopener">10.5281/zenodo.17358327</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">mouse-sc-rnaseq</span> <span class="tag-pill">other-mouse</span> <span class="tag-pill">schlossmacher</span></p>
          <p><strong>Keywords:</strong> mouse-sc-rnaseq, other-mouse, schlossmacher</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.1</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-schlossmacher-mouse-sn-rnaseq-osn-aav-transd</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-sulzer-fecal-metagenome-fp-spf-52" data-search="sulzer-fecal-metagenome-fp-spf oral treatment of thy1-aso mice with faecalibacterium prausnitzii a number of microbial taxa have been found to be reduced in parkinson&#x27;s disease (pd). treatment of α-synuclein overxpressing (thy1-aso) mice, an animal model of pd, with these taxa has also been shown to improve motor and gi deficits. this dataset focuses on one of the reduced taxa, faecalibacterium prausnitzii, and the effect of providing it as an oral treatment to both thy1-aso mice and wild-type controls. na cc-by-4.0 10.5281/zenodo.18989559 fecal-metagenome sulzer fecal-metagenome sulzer gs://asap-raw-team-sulzer-fecal-metagenome-fp-spf gs://asap-dev-team-sulzer-fecal-metagenome-fp-spf gs://asap-uat-team-sulzer-fecal-metagenome-fp-spf gs://asap-curated-team-sulzer-fecal-metagenome-fp-spf v4.0.2 v4.0.2 v1.0 v4.3" data-tags="fecal-metagenome||sulzer">
      <td><code>sulzer-fecal-metagenome-fp-spf</code></td>
      <td>Oral treatment of Thy1-ASO mice with Faecalibacterium prausnitzii</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.0.2</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-sulzer-fecal-metagenome-fp-spf-52">View</button></td>
    </tr>
    <tr id="dataset-detail-sulzer-fecal-metagenome-fp-spf-52" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Oral treatment of Thy1-ASO mice with Faecalibacterium prausnitzii</h3>
          <p><strong>Dataset ID:</strong> <code>sulzer-fecal-metagenome-fp-spf</code></p>
          <p><strong>Description:</strong> A number of microbial taxa have been found to be reduced in Parkinson&#x27;s disease (PD). Treatment of α-synuclein overxpressing (Thy1-ASO) mice, an animal model of PD, with these taxa has also been shown to improve motor and GI deficits. This dataset focuses on one of the reduced taxa, Faecalibacterium prausnitzii, and the effect of providing it as an oral treatment to both Thy1-ASO mice and wild-type controls.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.0.2</p>
          <p><strong>Latest CDE version:</strong> v4.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18989559" target="_blank" rel="noopener">10.5281/zenodo.18989559</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">fecal-metagenome</span> <span class="tag-pill">sulzer</span></p>
          <p><strong>Keywords:</strong> fecal-metagenome, sulzer</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.0.2</td>
                <td>v1.0</td>
                <td>v4.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-sulzer-fecal-metagenome-fp-spf</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-sulzer-fecal-metagenome-fp-spf</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-sulzer-fecal-metagenome-fp-spf</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-sulzer-fecal-metagenome-fp-spf</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-sulzer-pmdbs-sn-rnaseq-53" data-search="sulzer-pmdbs-sn-rnaseq single-nucleus rnaseq of the post-mortem cingulate cortex and substantia nigra from control and parkinson&#x27;s disease brains samples of the cingulate cortex and substantia nigra from  post-mortem brains from the new york brain bank were dissected and processed using 10x single-nucleus rna sequencing on the  chromium next gem single cell v3.1 (dual index) platform. pmdbs-sc-rnaseq cc-by-4.0 10.5281/zenodo.17612853 pmdbs-sc-rnaseq sulzer pmdbs-sc-rnaseq pmdbs-sc-rnaseq sulzer gs://asap-raw-team-sulzer-pmdbs-sn-rnaseq gs://asap-dev-team-sulzer-pmdbs-sn-rnaseq gs://asap-uat-team-sulzer-pmdbs-sn-rnaseq gs://asap-curated-team-sulzer-pmdbs-sn-rnaseq v4.0.0 v4.1.0 v4.0.0 v1.0 v3.3 v4.1.0 v1.1 v3.3" data-tags="pmdbs-sc-rnaseq||sulzer">
      <td><code>sulzer-pmdbs-sn-rnaseq</code></td>
      <td>Single-nucleus RNAseq of the post-mortem cingulate cortex and substantia nigra from control and Parkinson&#x27;s disease brains</td>
      <td>pmdbs-sc-rnaseq</td>
      <td>v1.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-sulzer-pmdbs-sn-rnaseq-53">View</button></td>
    </tr>
    <tr id="dataset-detail-sulzer-pmdbs-sn-rnaseq-53" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single-nucleus RNAseq of the post-mortem cingulate cortex and substantia nigra from control and Parkinson&#x27;s disease brains</h3>
          <p><strong>Dataset ID:</strong> <code>sulzer-pmdbs-sn-rnaseq</code></p>
          <p><strong>Description:</strong> Samples of the Cingulate Cortex and Substantia Nigra from  post-mortem brains from the New York Brain Bank were dissected and processed using 10X single-nucleus RNA sequencing on the  Chromium Next GEM Single Cell v3.1 (Dual Index) platform.</p>
          <p><strong>Collection:</strong> pmdbs-sc-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.17612853" target="_blank" rel="noopener">10.5281/zenodo.17612853</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs-sc-rnaseq</span> <span class="tag-pill">sulzer</span></p>
          <p><strong>Keywords:</strong> pmdbs-sc-rnaseq, pmdbs-sc-rnaseq, sulzer</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-sulzer-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-sulzer-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-sulzer-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-sulzer-pmdbs-sn-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-voet-pmdbs-sn-atacseq-10x-54" data-search="voet-pmdbs-sn-atacseq-10x single nuclei atac sequencing of postmortem cingulate cortex and midbrain of healthy donors and parkinson&#x27;s disease patients – 10x snatac-seq. this dataset consists of raw sequencing snatac-seq data (10x genomics chromium next gem single cell atac v2). the data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). the protocol followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. to increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. to computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108) has been used. the population vcf with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors. (edited) na cc-by-4.0 10.5281/zenodo.18988729 pmdbs sn-atacseq voet pmdbs sn-atacseq voet gs://asap-raw-team-voet-pmdbs-sn-atacseq-10x gs://asap-dev-team-voet-pmdbs-sn-atacseq-10x gs://asap-uat-team-voet-pmdbs-sn-atacseq-10x gs://asap-curated-team-voet-pmdbs-sn-atacseq-10x v4.1.1 v4.1.1 v1.0 v4.4" data-tags="pmdbs||sn-atacseq||voet">
      <td><code>voet-pmdbs-sn-atacseq-10x</code></td>
      <td>Single nuclei ATAC sequencing of postmortem cingulate cortex and midbrain of healthy donors and Parkinson&#x27;s disease patients – 10x snATAC-seq.</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-voet-pmdbs-sn-atacseq-10x-54">View</button></td>
    </tr>
    <tr id="dataset-detail-voet-pmdbs-sn-atacseq-10x-54" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single nuclei ATAC sequencing of postmortem cingulate cortex and midbrain of healthy donors and Parkinson&#x27;s disease patients – 10x snATAC-seq.</h3>
          <p><strong>Dataset ID:</strong> <code>voet-pmdbs-sn-atacseq-10x</code></p>
          <p><strong>Description:</strong> This dataset consists of raw sequencing snATAC-seq data (10x Genomics Chromium Next GEM Single Cell ATAC v2). The data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with Parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). The protocol followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. To increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. To computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108) has been used. The population VCF with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors. (edited)</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.1</p>
          <p><strong>Latest CDE version:</strong> v4.4</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18988729" target="_blank" rel="noopener">10.5281/zenodo.18988729</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs</span> <span class="tag-pill">sn-atacseq</span> <span class="tag-pill">voet</span></p>
          <p><strong>Keywords:</strong> pmdbs, sn-atacseq, voet</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.1</td>
                <td>v1.0</td>
                <td>v4.4</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-voet-pmdbs-sn-atacseq-10x</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-voet-pmdbs-sn-atacseq-10x</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-voet-pmdbs-sn-atacseq-10x</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-voet-pmdbs-sn-atacseq-10x</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-voet-pmdbs-sn-atacseq-hydrop-55" data-search="voet-pmdbs-sn-atacseq-hydrop single nuclei atac sequencing of postmortem cingulate cortex of healthy donors and parkinson&#x27;s disease patients – hydrop-atac v2 this dataset consists of raw sequencing snatac-seq data (hydrop v2). the data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). the protocol followed to isolate nuclei from postmortem brain samples can be found below. to increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. to computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108) has been used. the population vcf with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors. na cc-by-4.0 10.5281/zenodo.18988735 pmdbs sn-atacseq voet pmdbs sn-atacseq voet gs://asap-raw-team-voet-pmdbs-sn-atacseq-hydrop gs://asap-dev-team-voet-pmdbs-sn-atacseq-hydrop gs://asap-uat-team-voet-pmdbs-sn-atacseq-hydrop gs://asap-curated-team-voet-pmdbs-sn-atacseq-hydrop v4.1.1 v4.1.1 v1.0 v4.4" data-tags="pmdbs||sn-atacseq||voet">
      <td><code>voet-pmdbs-sn-atacseq-hydrop</code></td>
      <td>Single nuclei ATAC sequencing of postmortem cingulate cortex of healthy donors and Parkinson&#x27;s disease patients – HyDrop-ATAC v2</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-voet-pmdbs-sn-atacseq-hydrop-55">View</button></td>
    </tr>
    <tr id="dataset-detail-voet-pmdbs-sn-atacseq-hydrop-55" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single nuclei ATAC sequencing of postmortem cingulate cortex of healthy donors and Parkinson&#x27;s disease patients – HyDrop-ATAC v2</h3>
          <p><strong>Dataset ID:</strong> <code>voet-pmdbs-sn-atacseq-hydrop</code></p>
          <p><strong>Description:</strong> This dataset consists of raw sequencing snATAC-seq data (HyDrop v2). The data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with Parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). The protocol followed to isolate nuclei from postmortem brain samples can be found below. To increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. To computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108) has been used. The population VCF with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.1</p>
          <p><strong>Latest CDE version:</strong> v4.4</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18988735" target="_blank" rel="noopener">10.5281/zenodo.18988735</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs</span> <span class="tag-pill">sn-atacseq</span> <span class="tag-pill">voet</span></p>
          <p><strong>Keywords:</strong> pmdbs, sn-atacseq, voet</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.1</td>
                <td>v1.0</td>
                <td>v4.4</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-voet-pmdbs-sn-atacseq-hydrop</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-voet-pmdbs-sn-atacseq-hydrop</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-voet-pmdbs-sn-atacseq-hydrop</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-voet-pmdbs-sn-atacseq-hydrop</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-voet-pmdbs-sn-atacseq-scalebio-10x-56" data-search="voet-pmdbs-sn-atacseq-scalebio-10x single nuclei atac sequencing of postmortem cingulate cortex and midbrain of healthy donors and parkinson&#x27;s disease patients – scale-atac + 10x genomics. this dataset consists of raw sequencing atac-seq data (scale-atac pre-indexing followed by 10x genomics snatac v2). the data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). the protocol followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. to increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. to computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108) has been used. the population vcf with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors. na cc-by-4.0 10.5281/zenodo.18988717 pmdbs sn-atacseq voet pmdbs sn-atacseq voet gs://asap-raw-team-voet-pmdbs-sn-atacseq-scalebio-10x gs://asap-dev-team-voet-pmdbs-sn-atacseq-scalebio-10x gs://asap-uat-team-voet-pmdbs-sn-atacseq-scalebio-10x gs://asap-curated-team-voet-pmdbs-sn-atacseq-scalebio-10x v4.1.1 v4.1.1 v1.0 v4.4" data-tags="pmdbs||sn-atacseq||voet">
      <td><code>voet-pmdbs-sn-atacseq-scalebio-10x</code></td>
      <td>Single nuclei ATAC sequencing of postmortem cingulate cortex and midbrain of healthy donors and Parkinson&#x27;s disease patients – Scale-ATAC + 10x Genomics.</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-voet-pmdbs-sn-atacseq-scalebio-10x-56">View</button></td>
    </tr>
    <tr id="dataset-detail-voet-pmdbs-sn-atacseq-scalebio-10x-56" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single nuclei ATAC sequencing of postmortem cingulate cortex and midbrain of healthy donors and Parkinson&#x27;s disease patients – Scale-ATAC + 10x Genomics.</h3>
          <p><strong>Dataset ID:</strong> <code>voet-pmdbs-sn-atacseq-scalebio-10x</code></p>
          <p><strong>Description:</strong> This dataset consists of raw sequencing ATAC-seq data (Scale-ATAC pre-indexing followed by 10x Genomics snATAC v2). The data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with Parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). The protocol followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. To increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. To computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108) has been used. The population VCF with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.1</p>
          <p><strong>Latest CDE version:</strong> v4.4</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18988717" target="_blank" rel="noopener">10.5281/zenodo.18988717</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs</span> <span class="tag-pill">sn-atacseq</span> <span class="tag-pill">voet</span></p>
          <p><strong>Keywords:</strong> pmdbs, sn-atacseq, voet</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.1</td>
                <td>v1.0</td>
                <td>v4.4</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-voet-pmdbs-sn-atacseq-scalebio-10x</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-voet-pmdbs-sn-atacseq-scalebio-10x</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-voet-pmdbs-sn-atacseq-scalebio-10x</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-voet-pmdbs-sn-atacseq-scalebio-10x</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-voet-pmdbs-sn-atacseq-scalebio-hydrop-57" data-search="voet-pmdbs-sn-atacseq-scalebio-hydrop single nuclei atac sequencing of postmortem cingulate cortex of healthy donors – scale-atac + hydrop v2. this dataset consists of raw sequencing atac-seq data (scale-atac + hydrop v2). the data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). the protocols followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. to increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. to computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108 ) has been used. the population vcf with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors. na cc-by-4.0 10.5281/zenodo.18988743 pmdbs sn-atacseq voet pmdbs sn-atacseq voet gs://asap-raw-team-voet-pmdbs-sn-atacseq-scalebio-hydrop gs://asap-dev-team-voet-pmdbs-sn-atacseq-scalebio-hydrop gs://asap-uat-team-voet-pmdbs-sn-atacseq-scalebio-hydrop gs://asap-curated-team-voet-pmdbs-sn-atacseq-scalebio-hydrop v4.1.1 v4.1.1 v1.0 v4.4" data-tags="pmdbs||sn-atacseq||voet">
      <td><code>voet-pmdbs-sn-atacseq-scalebio-hydrop</code></td>
      <td>Single nuclei ATAC sequencing of postmortem cingulate cortex of healthy donors – Scale-ATAC + HyDrop v2.</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-voet-pmdbs-sn-atacseq-scalebio-hydrop-57">View</button></td>
    </tr>
    <tr id="dataset-detail-voet-pmdbs-sn-atacseq-scalebio-hydrop-57" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single nuclei ATAC sequencing of postmortem cingulate cortex of healthy donors – Scale-ATAC + HyDrop v2.</h3>
          <p><strong>Dataset ID:</strong> <code>voet-pmdbs-sn-atacseq-scalebio-hydrop</code></p>
          <p><strong>Description:</strong> This dataset consists of raw sequencing ATAC-seq data (Scale-ATAC + HyDrop v2). The data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with Parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). The protocols followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. To increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. To computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108 ) has been used. The population VCF with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.1</p>
          <p><strong>Latest CDE version:</strong> v4.4</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18988743" target="_blank" rel="noopener">10.5281/zenodo.18988743</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs</span> <span class="tag-pill">sn-atacseq</span> <span class="tag-pill">voet</span></p>
          <p><strong>Keywords:</strong> pmdbs, sn-atacseq, voet</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.1</td>
                <td>v1.0</td>
                <td>v4.4</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-voet-pmdbs-sn-atacseq-scalebio-hydrop</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-voet-pmdbs-sn-atacseq-scalebio-hydrop</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-voet-pmdbs-sn-atacseq-scalebio-hydrop</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-voet-pmdbs-sn-atacseq-scalebio-hydrop</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-voet-pmdbs-sn-multimodal-58" data-search="voet-pmdbs-sn-multimodal single nuclei rna sequencing of postmortem cingulate cortex, midbrain and motor cortex of healthy donors and parkinson&#x27;s disease patients – 10x multiome (snrna-seq and snatac-seq). this dataset consists of raw sequencing snrna-seq data and snatac-seq data (10x genomics chromium next gem multiome atac/gex). the data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). the protocol followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. to increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. to computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108 ) has been used. the population vcf with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors. (edited) na cc-by-4.0 10.5281/zenodo.18988753 pmdbs sn-multimodal voet pmdbs sn-multimodal voet gs://asap-raw-team-voet-pmdbs-sn-multimodal gs://asap-dev-team-voet-pmdbs-sn-multimodal gs://asap-uat-team-voet-pmdbs-sn-multimodal gs://asap-curated-team-voet-pmdbs-sn-multimodal v4.1.1 v4.1.1 v1.0 v4.4" data-tags="pmdbs||sn-multimodal||voet">
      <td><code>voet-pmdbs-sn-multimodal</code></td>
      <td>Single nuclei RNA sequencing of postmortem cingulate cortex, midbrain and motor cortex of healthy donors and Parkinson&#x27;s disease patients – 10x multiome (snRNA-seq and snATAC-seq).</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-voet-pmdbs-sn-multimodal-58">View</button></td>
    </tr>
    <tr id="dataset-detail-voet-pmdbs-sn-multimodal-58" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single nuclei RNA sequencing of postmortem cingulate cortex, midbrain and motor cortex of healthy donors and Parkinson&#x27;s disease patients – 10x multiome (snRNA-seq and snATAC-seq).</h3>
          <p><strong>Dataset ID:</strong> <code>voet-pmdbs-sn-multimodal</code></p>
          <p><strong>Description:</strong> This dataset consists of raw sequencing snRNA-seq data and snATAC-seq data (10x Genomics Chromium Next GEM Multiome ATAC/GEX). The data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with Parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). The protocol followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. To increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. To computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108 ) has been used. The population VCF with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors. (edited)</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.1</p>
          <p><strong>Latest CDE version:</strong> v4.4</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18988753" target="_blank" rel="noopener">10.5281/zenodo.18988753</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs</span> <span class="tag-pill">sn-multimodal</span> <span class="tag-pill">voet</span></p>
          <p><strong>Keywords:</strong> pmdbs, sn-multimodal, voet</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.1</td>
                <td>v1.0</td>
                <td>v4.4</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-voet-pmdbs-sn-multimodal</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-voet-pmdbs-sn-multimodal</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-voet-pmdbs-sn-multimodal</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-voet-pmdbs-sn-multimodal</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-voet-pmdbs-sn-rnaseq-59" data-search="voet-pmdbs-sn-rnaseq single nuclei rna sequencing (10x) of postmortem cingulate cortex and midbrain of healthy donors and parkinson&#x27;s disease patients – 10x snrna-seq. this dataset consists of raw sequencing snrna-seq data (10x genomics chromium next gem single cell 3ʹ). the data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). the protocol followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. to increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. to computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108) has been used. the population vcf with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors. na cc-by-4.0 10.5281/zenodo.18988768 pmdbs sn-rnaseq voet pmdbs sn-rnaseq voet gs://asap-raw-team-voet-pmdbs-sn-rnaseq gs://asap-dev-team-voet-pmdbs-sn-rnaseq gs://asap-uat-team-voet-pmdbs-sn-rnaseq gs://asap-curated-team-voet-pmdbs-sn-rnaseq v4.1.1 v4.1.1 v1.0 v4.4" data-tags="pmdbs||sn-rnaseq||voet">
      <td><code>voet-pmdbs-sn-rnaseq</code></td>
      <td>Single nuclei RNA sequencing (10x) of postmortem cingulate cortex and midbrain of healthy donors and Parkinson&#x27;s disease patients – 10x snRNA-seq.</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-voet-pmdbs-sn-rnaseq-59">View</button></td>
    </tr>
    <tr id="dataset-detail-voet-pmdbs-sn-rnaseq-59" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single nuclei RNA sequencing (10x) of postmortem cingulate cortex and midbrain of healthy donors and Parkinson&#x27;s disease patients – 10x snRNA-seq.</h3>
          <p><strong>Dataset ID:</strong> <code>voet-pmdbs-sn-rnaseq</code></p>
          <p><strong>Description:</strong> This dataset consists of raw sequencing snRNA-seq data (10x Genomics Chromium Next GEM Single Cell 3ʹ). The data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with Parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). The protocol followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. To increase throughput and to decrease batch effects, several donors have been pooled together into a single sequencing library. To computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108) has been used. The population VCF with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.1</p>
          <p><strong>Latest CDE version:</strong> v4.4</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18988768" target="_blank" rel="noopener">10.5281/zenodo.18988768</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs</span> <span class="tag-pill">sn-rnaseq</span> <span class="tag-pill">voet</span></p>
          <p><strong>Keywords:</strong> pmdbs, sn-rnaseq, voet</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.1</td>
                <td>v1.0</td>
                <td>v4.4</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-voet-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-voet-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-voet-pmdbs-sn-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-voet-pmdbs-sn-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-voet-pmdbs-sn-rnaseq-parsebio-60" data-search="voet-pmdbs-sn-rnaseq-parsebio single nuclei rna sequencing (parsebio) of postmortem cingulate cortex and midbrain of healthy donors and parkinson&#x27;s disease patients. this dataset consists of raw sequencing snrna-seq data using parsebio evercode whole transcriptome. the data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). the protocol followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. to increase throughput and to decrease batch effects, several donors have been pooled together into a specific parsebio barcode. to computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108) has been used. the population vcf with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors. na cc-by-4.0 10.5281/zenodo.18988761 pmdbs sn-rnaseq voet pmdbs sn-rnaseq voet gs://asap-raw-team-voet-pmdbs-sn-rnaseq-parsebio gs://asap-dev-team-voet-pmdbs-sn-rnaseq-parsebio gs://asap-uat-team-voet-pmdbs-sn-rnaseq-parsebio gs://asap-curated-team-voet-pmdbs-sn-rnaseq-parsebio v4.1.1 v4.1.1 v1.0 v4.4" data-tags="pmdbs||sn-rnaseq||voet">
      <td><code>voet-pmdbs-sn-rnaseq-parsebio</code></td>
      <td>Single nuclei RNA sequencing (ParseBio) of postmortem cingulate cortex and midbrain of healthy donors and Parkinson&#x27;s disease patients.</td>
      <td>NA</td>
      <td>v1.0</td>
      <td>v4.1.1</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-voet-pmdbs-sn-rnaseq-parsebio-60">View</button></td>
    </tr>
    <tr id="dataset-detail-voet-pmdbs-sn-rnaseq-parsebio-60" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Single nuclei RNA sequencing (ParseBio) of postmortem cingulate cortex and midbrain of healthy donors and Parkinson&#x27;s disease patients.</h3>
          <p><strong>Dataset ID:</strong> <code>voet-pmdbs-sn-rnaseq-parsebio</code></p>
          <p><strong>Description:</strong> This dataset consists of raw sequencing snRNA-seq data using ParseBio Evercode Whole Transcriptome. The data is part of an overall set of samples derived from postmortem midbrain (n=140), cingulate cortex (n=190) and motor cortex (n=4) of healthy donors (n=114), patients with Parkinson&#x27;s disease (n=75) or patients with other neurological disorder (n=1). The protocol followed to isolate nuclei from postmortem brain samples and to prepare sequencing libraries can be found below. To increase throughput and to decrease batch effects, several donors have been pooled together into a specific ParseBio barcode. To computationally demultiplex the nuclei to their corresponding donors, cellsnp-lite (version commit: aad18644adcde853c313362a856a24245c9b91f7) followed by vireo (https://github.com/single-cell-genetics/vireo/pull/108) has been used. The population VCF with the donor genotypes derived from whole genome sequencing data has been used to assign nuclei back to their donors.</p>
          <p><strong>Collection:</strong> NA</p>
          <p><strong>Current dataset version:</strong> v1.0</p>
          <p><strong>Latest release:</strong> v4.1.1</p>
          <p><strong>Latest CDE version:</strong> v4.4</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.18988761" target="_blank" rel="noopener">10.5281/zenodo.18988761</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs</span> <span class="tag-pill">sn-rnaseq</span> <span class="tag-pill">voet</span></p>
          <p><strong>Keywords:</strong> pmdbs, sn-rnaseq, voet</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.1</td>
                <td>v1.0</td>
                <td>v4.4</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-voet-pmdbs-sn-rnaseq-parsebio</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-voet-pmdbs-sn-rnaseq-parsebio</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-voet-pmdbs-sn-rnaseq-parsebio</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-voet-pmdbs-sn-rnaseq-parsebio</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
    <tr class="dataset-row" data-detail="dataset-detail-wood-pmdbs-bulk-rnaseq-61" data-search="wood-pmdbs-bulk-rnaseq bulk rna sequencing of human post-mortem brain tissue from parkinson&#x27;s disease and control donors bulk rna-seq data from 234 samples derived from pmdbs samples across substantia nigra, caudate, putamen, parahippocampal gyrus, cingulate cortex, temporal cortex, frontal cortex, parietal cortex types of samples: (braak 3-4) pd and control post-mortem brains. https://github.com/jbrenton191/rnaseq_splicing_pipeline pmdbs-bulk-rnaseq cc-by-4.0 10.5281/zenodo.16749007 pmdbs-bulk-rnaseq wood pmdbs-bulk-rnaseq pmdbs-bulk-rnaseq wood gs://asap-raw-team-wood-pmdbs-bulk-rnaseq gs://asap-dev-team-wood-pmdbs-bulk-rnaseq gs://asap-uat-team-wood-pmdbs-bulk-rnaseq gs://asap-curated-team-wood-pmdbs-bulk-rnaseq v2.0.0 v3.0.0 v4.0.0 v4.1.0 v2.0.0 v1.0 v3.0 v3.0.0 v1.0 v3.2 v4.0.0 v1.0 v3.3 v4.1.0 v1.1 v3.3" data-tags="pmdbs-bulk-rnaseq||wood">
      <td><code>wood-pmdbs-bulk-rnaseq</code></td>
      <td>Bulk RNA sequencing of human post-mortem brain tissue from Parkinson&#x27;s disease and control donors</td>
      <td>pmdbs-bulk-rnaseq</td>
      <td>v1.1</td>
      <td>v4.1.0</td>
      <td><button class="dataset-toggle" data-target="dataset-detail-wood-pmdbs-bulk-rnaseq-61">View</button></td>
    </tr>
    <tr id="dataset-detail-wood-pmdbs-bulk-rnaseq-61" class="dataset-detail-row">
      <td colspan="6">
        <div class="dataset-detail">
          <h3>Bulk RNA sequencing of human post-mortem brain tissue from Parkinson&#x27;s disease and control donors</h3>
          <p><strong>Dataset ID:</strong> <code>wood-pmdbs-bulk-rnaseq</code></p>
          <p><strong>Description:</strong> Bulk RNA-seq data from 234 samples derived from PMDBS samples across Substantia Nigra, Caudate, Putamen, Parahippocampal Gyrus, Cingulate Cortex, Temporal Cortex, Frontal Cortex, Parietal Cortex Types of Samples: (Braak 3-4) PD and control post-mortem brains. https://github.com/Jbrenton191/RNAseq_splicing_pipeline</p>
          <p><strong>Collection:</strong> pmdbs-bulk-rnaseq</p>
          <p><strong>Current dataset version:</strong> v1.1</p>
          <p><strong>Latest release:</strong> v4.1.0</p>
          <p><strong>Latest CDE version:</strong> v3.3</p>
          <p><strong>License:</strong> CC-BY-4.0</p>
          <p><strong>DOI:</strong> <a href="https://doi.org/10.5281/zenodo.16749007" target="_blank" rel="noopener">10.5281/zenodo.16749007</a></p>
          <p><strong>Tags:</strong> <span class="tag-pill">pmdbs-bulk-rnaseq</span> <span class="tag-pill">wood</span></p>
          <p><strong>Keywords:</strong> pmdbs-bulk-rnaseq, pmdbs-bulk-rnaseq, wood</p>
          <h4>Release history</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Release</th>
                <th>Dataset version</th>
                <th>CDE version</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>v4.1.0</td>
                <td>v1.1</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v4.0.0</td>
                <td>v1.0</td>
                <td>v3.3</td>
              </tr>
              <tr>
                <td>v3.0.0</td>
                <td>v1.0</td>
                <td>v3.2</td>
              </tr>
              <tr>
                <td>v2.0.0</td>
                <td>v1.0</td>
                <td>v3.0</td>
              </tr>
            </tbody>
          </table>
          <h4>Bucket paths</h4>
          <table class="mini-table">
            <thead>
              <tr>
                <th>Environment</th>
                <th>Bucket path</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>raw</td>
                <td><code>gs://asap-raw-team-wood-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>dev</td>
                <td><code>gs://asap-dev-team-wood-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>uat</td>
                <td><code>gs://asap-uat-team-wood-pmdbs-bulk-rnaseq</code></td>
              </tr>
              <tr>
                <td>prod</td>
                <td><code>gs://asap-curated-team-wood-pmdbs-bulk-rnaseq</code></td>
              </tr>
            </tbody>
          </table>
        </div>
      </td>
    </tr>
  </tbody>
</table>
