import configparser
from pathlib import Path

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_path = Path("config.ini")
        
        if not self.config_path.exists():
            self.create_default_config()
        
        self.config.read(self.config_path)
    
    def create_default_config(self):
        self.config["API"] = {
            "google_maps_api_key": "YOUR_API_KEY_HERE"
        }
        
        self.config["DATABASE"] = {
            "path": "data/business_data.db"
        }
        
        with open(self.config_path, "w") as f:
            self.config.write(f)
    
    def get(self, key, section="API"):
        return self.config[section][key] 