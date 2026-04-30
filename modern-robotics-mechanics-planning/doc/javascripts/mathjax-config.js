/* MathJax 3: load this file BEFORE tex-mml-chtml.js (see mkdocs.yml).
   Aligned with Material for MkDocs official math reference:
   https://squidfunk.github.io/mkdocs-material/reference/math/ */
window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [
      ['\\[', '\\]'],
      ['$$', '$$']
    ],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    /* Note: `".*|"` (with trailing |) is what upstream Material docs use, not `".*"` */
    ignoreHtmlClass: '.*|',
    processHtmlClass: 'arithmatex'
  }
};

/* Re-typeset when using Material features that swap page content (e.g. instant navigation). */
if (typeof document$ !== 'undefined' && document$ && typeof document$.subscribe === 'function') {
  document$.subscribe(() => {
    if (!window.MathJax) return;
    if (MathJax.startup && MathJax.startup.output && typeof MathJax.startup.output.clearCache === 'function') {
      MathJax.startup.output.clearCache();
    }
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise();
  });
}
