# Code review application
## About program
This is a simple Python application, built using Tkinter that allows you to compare text in two windows and generate an HTML report highlighting the differences like such as adding, deleting, changing an element in the file. The main purpose of creating this application was simplification of code review and finding modifications made to the code beyond the confirmed update. Then collect all of the findings in html report that can be converted e.g. to pdf file.

## Features
- Two Text Windows: Enter the original code and the updated code in separate text windows.
- Comparison Results: View the differences between the two sets of code in a third window.
- Clear Function: Clear the content of both code windows with a single click.
- Generate HTML Report: Generate an HTML report highlighting the differences between the two code snippets.
## Requirements

| Tool | Version |
| ------ | ------ |
| Python| 3.x |
| Tkinter | 0.1.0 |

## Installation
Clone the repository: git clone https://github.com/your-username/code-review-app.git
Navigate to the application directory: cd code-review-app
## How to Run
Run the application: python main.py
Enter the original code in the left window and the updated code in the right window.
Click the "Compare and display" button to see the differences in the third window.
Click the "Generate Report" button to create an HTML report with the comparison results.
Use the "Clear Both Boxes" button to clear the content in both code windows.

##HTML Report
The HTML report (show_comparison.html) will be generated in the application directory. Open the report in a web browser to view detailed differences between the original and updated code.

## License
MIT
