from pathlib import Path

class MarkdownTable:

    def __init__(self, dataframe):

        self.dataframe = dataframe

        for key, detail in dataframe.items():
            self.headings = [hd for hd in detail]
            break

        self.markdown = ''

    def set_section_heading(self, heading):

        self.markdown = f'# {heading}\n\n' + self.markdown

    def get_col_width(self):

        # A dictionary to contain the length of each component string
        # so that the output Markdown table can be properly formatted
        col_width = {}
        for heading in self.headings:
            col_width[heading] = len(heading)

        for df_heading, df_details in self.dataframe.items():
            for heading, value in df_details.items():
                if len(value) > col_width[heading]:
                    col_width[heading] = len(value)

        return col_width

    def make_table(self):

        # Calculate the column width of each
        col_width = self.get_col_width()

        # Construct the Markdown table header
        self.markdown += '| ' + ' | '.join(
            [hd.title().ljust(col_width[hd]) for hd in self.headings]) + ' |\n'
        self.markdown += '| ' + ' | '.join(
            ["-" * col_width[hd] for hd in self.headings]) + ' |\n'

        # Loop through the dataframe
        for df_heading, df_details in self.dataframe.items():
            self.markdown += '| ' + ' | '.join(
                [df_details[hd].ljust(col_width[hd]) for hd in
                 self.headings]) + ' |\n'

        return self.markdown

    def save(self, path):
        # Construct and create the output directory
        output_folder = Path(path)
        output_folder.mkdir(parents=True, exist_ok=True)
        output_file = output_folder / f'markdown-table.md'

        # Save the final markdown output to file
        with open(output_file, 'w') as md_f_stream:
            md_f_stream.write(self.markdown)

        return True
