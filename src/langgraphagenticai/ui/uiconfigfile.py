from configparser import ConfigParser

class UIConfigFile:
    def __init__(self, config_file_path="src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file_path)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(', ')

    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(', ')

    def get_model_options(self):
        return self.config["DEFAULT"].get("MODEL_OPTIONS").split(', ')

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")