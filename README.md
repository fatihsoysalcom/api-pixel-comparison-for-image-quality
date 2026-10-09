# API Pixel Comparison for Image Quality

This Python script demonstrates pixel-level comparison between two image files. It's designed to be used in API acceptance tests for image processing services, ensuring that the generated images not only exist but also match a reference image within an acceptable tolerance.

## Language

`python`

## How to Run

1. Ensure you have Python and Pillow installed (`pip install Pillow`).
2. Save the code as `api_pixel_test.py`.
3. Create `reference.png` and `api_output.png` in the same directory (or modify paths in the script).
4. Run the script: `python api_pixel_test.py`.

## Original Article

This example accompanies the Turkish article: [API Kabul Testlerinde Piksel Kontrolü: Sadece Başarı Yeterli Mi?](https://fatihsoysal.com/blog/api-kabul-testlerinde-piksel-kontrolu-sadece-basari-yeterli-mi/).

## License

MIT — see [LICENSE](LICENSE).
