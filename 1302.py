# -*- coding: utf-8 -*-
"""1302

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s3dVA_iBbWgL3FjNDC0vX4cacmMYtPX5
"""

from IPython.display import display, HTML
import time

def surprise():
    answer = input("Quer uma surpresa? (sim/não): ").lower()

    if answer == "sim":
        display(HTML("<p style='font-size: 20px;'>Desculpa, meu amor </p>"))
        time.sleep(1)
        display(HTML("<p style='font-size: 30px; color: red;'>&#10084;</p>"))
    else:
        print("Sem surpresa. Talvez da próxima vez!")

surprise()