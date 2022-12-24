# url: https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
# problem: 2_mexicanWave.py

def wave(text):
  if len(text) == 0:
    return []
  waveList= []
  for i in range(len(text)):
    if text[i] == " ":
      continue
    waveList.append(text[0:i] + text[i].upper() + text[i+1:])
  return waveList