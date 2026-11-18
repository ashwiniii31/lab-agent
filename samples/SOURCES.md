# Sample sources

## public/ (20 files)
Dataset: [Shubhal829/high-quality-invoice-images-for-ocr](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr) on Hugging Face.
- Dataset card: "synthetic data only"; names, addresses and IDs are fictionally generated.
- Licence: ODbL (Open Database License) per the Hugging Face licence tag. The card also says "original license from Kaggle source". Attribution: Shubhal829 / original Kaggle authors.
- Used for: testing extraction on varied layouts. Not modified.

Per-file list (filled in automatically when the files were fetched):

- `public_01_batch1-0001.jpg` ← [data/batch1-0001.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0001.jpg) (ODbL)
- `public_02_batch1-0002.jpg` ← [data/batch1-0002.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0002.jpg) (ODbL)
- `public_03_batch1-0003.jpg` ← [data/batch1-0003.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0003.jpg) (ODbL)
- `public_04_batch1-0004.jpg` ← [data/batch1-0004.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0004.jpg) (ODbL)
- `public_05_batch1-0005.jpg` ← [data/batch1-0005.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0005.jpg) (ODbL)
- `public_06_batch1-0006.jpg` ← [data/batch1-0006.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0006.jpg) (ODbL)
- `public_07_batch1-0007.jpg` ← [data/batch1-0007.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0007.jpg) (ODbL)
- `public_08_batch1-0008.jpg` ← [data/batch1-0008.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0008.jpg) (ODbL)
- `public_09_batch1-0009.jpg` ← [data/batch1-0009.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0009.jpg) (ODbL)
- `public_10_batch1-0010.jpg` ← [data/batch1-0010.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0010.jpg) (ODbL)
- `public_11_batch1-0011.jpg` ← [data/batch1-0011.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0011.jpg) (ODbL)
- `public_12_batch1-0012.jpg` ← [data/batch1-0012.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0012.jpg) (ODbL)
- `public_13_batch1-0013.jpg` ← [data/batch1-0013.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0013.jpg) (ODbL)
- `public_14_batch1-0014.jpg` ← [data/batch1-0014.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0014.jpg) (ODbL)
- `public_15_batch1-0015.jpg` ← [data/batch1-0015.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0015.jpg) (ODbL)
- `public_16_batch1-0016.jpg` ← [data/batch1-0016.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0016.jpg) (ODbL)
- `public_17_batch1-0017.jpg` ← [data/batch1-0017.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0017.jpg) (ODbL)
- `public_18_batch1-0018.jpg` ← [data/batch1-0018.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0018.jpg) (ODbL)
- `public_19_batch1-0019.jpg` ← [data/batch1-0019.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0019.jpg) (ODbL)
- `public_20_batch1-0020.jpg` ← [data/batch1-0020.jpg](https://huggingface.co/datasets/Shubhal829/high-quality-invoice-images-for-ocr/blob/main/data/batch1-0020.jpg) (ODbL)

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
