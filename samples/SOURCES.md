# Sample sources

## public/ (20 files)
Dataset: [Shubhal829/high-quality-invoice-images-for-ocr](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr) on Hugging Face.
- Dataset card: "synthetic data only"; names, addresses and IDs are fictionally generated.
- Licence: ODbL (Open Database License) per the Hugging Face licence tag. The card also says "original license from Kaggle source". Attribution: Shubhal829 / original Kaggle authors.
- Used for: testing extraction on varied layouts. Not modified.

Per-file list (filled in automatically when the files were fetched):

<!-- PUBLIC_FILES -->

## edge/ (10 files)
Made by me, fictional data. Generated as PNGs for the 0.1 failure table.

| File | Tests | Failure-table row |
|------|-------|-------------------|
| edge_01_not_invoice.png | a restaurant menu, not an invoice | 2 |
| edge_02_blurry.png | invoice photographed out of focus | 1 |
| edge_03_euro_total.png | total written as "€4.500" (European format) | 4, 6 |
| edge_04_ambiguous_date.png | 03/04/2026 with no other date | 6 |
| edge_05_date_with_evidence.png | 03/04/2026 plus due date 25/04/2026 (proves DD/MM) | 6 |
| edge_06_sum_mismatch.png | line items sum to 4,500 but total says 4,800 | 5 |
| edge_07_missing_total.png | no total at all | 4 |
| edge_08_foreign_currency.png | USD invoice | currency handling |
| edge_09_handwritten.png | handwritten kirana bill | 1 |
| edge_10_two_totals.png | subtotal and grand total both shown | 4 |
