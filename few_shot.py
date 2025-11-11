import pandas as pd
import json


class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        try:
            with open(file_path, encoding="utf-8") as f:
                posts = json.load(f)
                self.df = pd.json_normalize(posts)
                self.df['length'] = self.df['line_count'].apply(self.categorize_length)
                # collect unique tags - use explode() to properly flatten lists
                all_tags = self.df['tags'].explode().dropna().unique().tolist()
                self.unique_tags = sorted(all_tags)  # Sort for consistent ordering
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {file_path}. Please ensure the file exists.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in file {file_path}: {e}")

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &  # Tags contain the specified tag
            (self.df['language'] == language) &  # Language matches
            (self.df['length'] == length)  # Length category matches (Short/Medium/Long)
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count <= 5:  # Changed to <= 5 to match "1 to 5 lines" in prompt
            return "Short"
        elif 6 <= line_count <= 10:  # Changed to start at 6 to match "6 to 10 lines" in prompt
            return "Medium"
        else:  # 11+ lines matches "11 to 15 lines" in prompt
            return "Long"

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()
    # print(fs.get_tags())
    posts = fs.get_filtered_posts("Medium","Hinglish","Job Search")
    print(posts)