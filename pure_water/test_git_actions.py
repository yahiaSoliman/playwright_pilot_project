import sys
import os

# Determine the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from data import Data


class TestGitActions:
    x = Data.change_owner_command_id_qa_stg

    def test_student_name(self):
        pass

    def test_student_age(self):
        pass
