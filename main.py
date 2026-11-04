# /// script
# requires-python = ">=3.9"
# dependencies = [pypdf]
# # Add dependency requirement strings to the array above as needed.
# ///

from pypdf import PdfWriter


def append_pdfs(pdf_list, output_filename):
    # Initialize the PDF writer
    writer = PdfWriter()

    # Loop through the files and append them
    for pdf in pdf_list:
        writer.append(pdf)

    # Save the combined PDF to a file
    with open(output_filename, "wb") as output_file:
        writer.write(output_file)

    # Clean up resources
    writer.close()


def main():
    files_to_merge = ["example.pdf"]
    append_pdfs(files_to_merge, "combined_output.pdf")
    print("PDFs appended successfully!")


if __name__ == "__main__":
    main()
