from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import sys
from src.logger import logging
from src.exception import CustomException

application=Flask(__name__)

app=application




# if __name__ == "__main__":

#     try:
#         1/0
#     except Exception as e:
#         logging.info("Divide by zero Error")
#         raise CustomException(e,sys)