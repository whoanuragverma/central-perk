# Needs tensorflow 1.15 and gpt-2 simple
# I will update this with my model or GPT-3 based on the need
# Trained Model is available on google drive and has file size around 900MB.


# GPT-2 works only with txt files so we need to merge them together
import gpt_2_simple as gpt2
import pandas as pd

df = pd.read_excel("data/dialouges.xlsx")
df = df.dropna()
df['Merge'] = df['Charcater']+": "+df['Dialouge']

with open("data/merged.txt", 'w') as f:
    for line in df['Merge']:
        f.write(str(line)+"\n")

# This creates a new file for further training
# This downloads around 500MB of model higher models cannot be trained on local machines

gpt2.download_gpt2(model_name="124M")

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              dataset='merged.txt',
              steps=1500,
              model_name='124M',
              restore_from='fresh',
              print_every=1,
              overwrite=True,
              sample_every=50,
              save_every=500,
              run_name='run1')

# This codeblock generates a text of length 1000.
# Lower the temperature the words will be more random
gpt2.generate(sess,
              run_name='run1',
              prefix='Monica: ',
              nsamples=1,
              length=1000,
              temperature=0.9)
