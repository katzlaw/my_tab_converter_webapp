import re
import os

def replace_date(match):
    year, month, day = match.groups()
    formatted_date = f"{int(month)}/{int(day)}/{year}"
    return formatted_date

def process_tab_content(tab_content, original_file_name):
    try:

        print('hello')
        
        # Split the tab content into lines
        tab_lines = tab_content.splitlines()

        # Initialize variables for modified content and other data
        modified_content = []
        number_of_slips = 0
        miss_suffix = ""
        found_id = ""

        for line in tab_lines:
            number_of_slips += 1
            line = line.replace(",,,,,,Time", "Time")
            
            if ",,,,,," in line:
                miss_suffix = "_miss"

            line = line.replace(",,,,,,", "\tFFFF\t").replace(",,,,,", "\t\t\t").replace(",,,", "\t")
            line = re.sub(r'\b(\d{4})(\d{2})(\d{2})\b', replace_date, line)
            id_pattern = r'\d{3}\.\w{4}'
            id_match = re.search(id_pattern, line)
            if id_match:
                print('i found matter number')
                found_id = id_match.group()

            modified_content.append(line)

        # Generate a modified file name
        filename, _ = os.path.splitext(original_file_name)
        modified_file_name = f"TSNB_{filename}_{found_id}_{number_of_slips}{miss_suffix}.txt"

        # Join the modified content
        modified_content = "\n".join(modified_content)

        # Save the processed content to the modified file name
        with open(modified_file_name, 'w') as txt_file:
            txt_file.write(modified_content)

        return modified_file_name
    
    except Exception as e:
        print(f"Error processing tab content: {str(e)}")
        return None
