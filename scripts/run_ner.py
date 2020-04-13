import ktrain
import matplotlib.pyplot as plt
from ktrain import text
import parameters
# Load data
(trn, val, preproc) = text.entities_from_txt(train_filepath=parameters.TRAIN_DATA, val_filepath=parameters.VALIDATION_DATA, data_format='conll2003')
# Load model
model = text.sequence_tagger('bilstm-bert', preproc, bert_model='monologg/biobert_v1.1_pubmed')
learner = ktrain.get_learner(model, train_data=trn, val_data=val, batch_size=128, eval_batch_size=64)

# Train using SGDR
learner.set_model(model)
learner.fit(1e-3, 3, cycle_len=1, cycle_mult=2, early_stopping=3)

# Validation
learner.validate()
learner.view_top_losses(n=1)
# Plot
learner.plot('lr')
learner.plot('loss')



plt.show(block=True)
plt.interactive(False)
