import openpyxl  # Importing the openpyxl library for working with Excel files
from openpyxl.styles import PatternFill, Font, Alignment  # Importing styles for formatting Excel cells
import pandas as pd  # Importing pandas for handling dataframes

class ExcelExporter:
    def __init__(self, detector):
        self.detector = detector  # Store the cheating detection object

    def parse_filename(self, filename):
        """Extracts name and ID from the filename."""
        try:
            name_id = filename.rsplit("_", 1)
            name = name_id[0]
            student_id = name_id[1].split(".")[0]
        except IndexError:
            name = filename
            student_id = "N/A"
        return name, student_id

    def export(self, output_file):
        # Placeholder dictionary for student scores
        students_scores = {}
        detailed_reports = []

        # Collect detailed cheating report
        report = self.detector.get_cheating_report()

        for line in report:
            try:
                if 'Possible cheating between' in line and 'with an overall score of' in line:
                    parts = line.split(' between ')[1].split(' with an overall score of ')
                    files = parts[0].split(' and ')
                    file1, file2 = files[0].strip(), files[1].strip()

                    similarity = float(parts[1].split(' and ML prediction')[0].strip())
                    ml_prediction = 1

                    name1, id1 = self.parse_filename(file1)
                    name2, id2 = self.parse_filename(file2)

                    students_scores[(name1, id1)] = max(students_scores.get((name1, id1), 0), similarity * 100)
                    students_scores[(name2, id2)] = max(students_scores.get((name2, id2), 0), similarity * 100)

                    detailed_reports.append((file1, file2, similarity, ml_prediction))

            except Exception as e:
                print(f"Error parsing line: {line} - {e}")

        # Prepare summary and detailed report DataFrames
        summary_data = []
        for (name, student_id), cheat_score in students_scores.items():
            final_grade = 0 if cheat_score == 100 else ''
            summary_data.append([name, student_id, '', cheat_score, final_grade])

        detailed_pairs_data = []
        for file1, file2, score, ml_prediction in detailed_reports:
            detailed_pairs_data.append(
                f'Possible cheating between {file1} and {file2} '
                f'with an overall score of {score:.2f} and ML prediction: {ml_prediction}'
            )

        summary_df = pd.DataFrame(summary_data, columns=['Name', 'ID', 'Actual Number', 'Cheat (%)', 'Final Grade'])
        detailed_pairs_df = pd.DataFrame(detailed_pairs_data, columns=['Detailed Report'])

        # Write to Excel
        try:
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                summary_df.to_excel(writer, sheet_name='Summary', index=False)

                worksheet = writer.sheets['Summary']

                # Define fill styles for alternating colors
                light_blue_fill = PatternFill(start_color='DCE6F1', end_color='DCE6F1', fill_type='solid')
                dark_blue_fill = PatternFill(start_color='A4C8E1', end_color='A4C8E1', fill_type='solid')

                # Center align and format headers
                header_font = Font(name='Arial', size=12, bold=True)
                header_fill = PatternFill(start_color='4F81BD', end_color='4F81BD', fill_type='solid')
                header_alignment = Alignment(horizontal='center', vertical='center')

                # Format headers
                for cell in worksheet[1]:
                    cell.font = header_font
                    cell.fill = header_fill
                    cell.alignment = header_alignment

                # Center align and format table content
                cell_font = Font(name='Arial', size=12)
                cell_alignment = Alignment(horizontal='center', vertical='center')

                # Apply styles to table rows
                for row_idx, row in enumerate(worksheet.iter_rows(min_row=2, max_row=worksheet.max_row,
                                                                  min_col=1, max_col=summary_df.shape[1]), start=2):
                    for col_idx, cell in enumerate(row, start=1):
                        cell.font = cell_font
                        cell.alignment = cell_alignment
                        # Apply alternating fill colors
                        if row_idx % 2 == 0:
                            cell.fill = light_blue_fill
                        else:
                            cell.fill = dark_blue_fill

                # Write detailed pairs report below the summary
                startrow = len(summary_df) + 3
                detailed_pairs_df.to_excel(writer, sheet_name='Summary', startrow=startrow, index=False)

                for index in range(len(detailed_pairs_df)):
                    worksheet.merge_cells(start_row=startrow + index + 1, start_column=1,
                                          end_row=startrow + index + 1, end_column=summary_df.shape[1])
                    cell = worksheet.cell(row=startrow + index + 1, column=1)
                    cell.value = detailed_pairs_df.iloc[index, 0]
                    cell.alignment = Alignment(horizontal='left', vertical='center')

                    # Apply alternating fill colors
                    if index % 2 == 0:
                        cell.fill = light_blue_fill
                    else:
                        cell.fill = dark_blue_fill

                    cell.font = Font(name='Arial', size=12, bold=False)

                # Adjust row height for better visibility
                for index in range(len(detailed_pairs_df)):
                    worksheet.row_dimensions[startrow + index + 1].height = 30

                # Add header style for the detailed report
                header_cell = worksheet.cell(row=startrow, column=1)
                header_cell.value = "Detailed Cheating Report"
                header_cell.font = Font(name='Arial', size=18, bold=True, color='FFFFFF')
                header_cell.fill = PatternFill(start_color='0530BB', end_color='0530BB', fill_type='solid')
                header_cell.alignment = Alignment(horizontal='center', vertical='center')

                worksheet.merge_cells(start_row=startrow, start_column=1, end_row=startrow,
                                      end_column=summary_df.shape[1])

                worksheet.column_dimensions['A'].width = 80

                last_index = startrow + len(detailed_pairs_df) + 1
                worksheet.merge_cells(start_row=last_index, start_column=1, end_row=last_index,
                                      end_column=summary_df.shape[1])
                last_cell = worksheet.cell(row=last_index, column=1)
                last_cell.value = "End of Detailed Cheating Report"
                last_cell.fill = PatternFill(start_color='0530BB', end_color='0530BB', fill_type='solid')
                last_cell.alignment = Alignment(horizontal='center', vertical='center')
                last_cell.font = Font(name='Arial', size=16, bold=True, color='FFFFFF')

                print(f"Excel file saved successfully at {output_file}")

        except Exception as e:
            print(f"Error writing to Excel: {e}")
