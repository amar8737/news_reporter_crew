import sys
import warnings
from datetime import datetime

from new_report_crew.crew import NewsReporterCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module='pysbd')
def run():

    """
    Main function to run the NewsReporterCrew process.
    """ 
    inputs ={
        "country": "INDIA"
    }
    try:
        crew_process = NewsReporterCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)