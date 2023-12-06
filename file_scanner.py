import os

class FileScanner:
    @staticmethod
    def get_strings(text_field_strings):
        textbox_content = text_field_strings.get("1.0", "end").strip().split()
        return set(textbox_content)

    @staticmethod
    def get_paths(text_field_paths):
        textbox_content = text_field_paths.get("1.0", "end").strip()
        if textbox_content:
            textbox_content = textbox_content.split("\n")
        else:
            textbox_content = set()
        paths = set()
        for path in textbox_content:
            if path not in paths:
                paths.add(path)
        return paths

    @staticmethod
    def filter_paths(paths):
        unfound_paths = set()
        found_paths = set()  
        for path in paths:
            if os.path.isfile(path):
                found_paths.add(path)
            else:
                unfound_paths.add(path)
        return unfound_paths, found_paths

    @staticmethod
    def match_strings(strings, found_paths):
        matched_paths = set()
        for path in found_paths:
            with open(path, "rb") as file:
                file_content = file.read()
            for string in strings:
                if bytes(string, encoding='utf-8') in file_content and file not in matched_paths:
                    matched_paths.add(path)
                    break
        return matched_paths