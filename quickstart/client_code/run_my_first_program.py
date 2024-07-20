from google.colab import output
from nada_dsl import *

def secret_addition():
   
  party1 = Party(name="Party1") 
  my_intl = SecretInteger(Input (name="my_int1", party=party1))
  my_int2 = SecretInteger(Input (name="my_int2", party=party1))
  result = my_int1 + my_int2
  Output (result, "my_output", party1)
  return[output]