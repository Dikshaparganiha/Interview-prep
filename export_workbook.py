from pathlib import Path
import runpy


if __name__ == "__main__":
    generator = Path(__file__).with_name("generate_question_database.py")
    runpy.run_path(str(generator), run_name="__main__")
