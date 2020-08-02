# Needs tensorflow 1.15 and gpt-2 simple

import gpt_2_simple as gpt2

# Trained and generated on Google Colaboratory
# Make sure the file is in the root directory of Google Drive

gpt2.copy_checkpoint_from_gdrive(run_name='run1')
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')

for i in tqdm(range(int(100))):
    file_name = 'scripts/script_' + str(i) + ".txt"
    gpt2.generate_to_file(sess, run_name='run1',
                          destination_path=file_name,
                          length=1000,
                          # Higher the temperature Crazier the text.
                          temperature=0.8
                          )
