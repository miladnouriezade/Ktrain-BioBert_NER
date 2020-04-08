import ktrain
import matplotlib.pyplot as plt
from ktrain import text
import parameters
# Load data
(trn, val, preproc) = text.entities_from_txt(train_filepath=parameters.TRAIN_DATA, val_filepath=parameters.VALIDATION_DATA, data_format='conll2003')
# Load model
model = text.sequence_tagger('bilstm-bert', preproc, bert_model='monologg/biobert_v1.1_pubmed')
learner = ktrain.get_learner(model, train_data=trn, val_data=val, batch_size=128, eval_batch_size=64)
# learner.lr_find()
# learner.lr_plot()

# Train
learner.set_model(model)

# training using the 1cycle policy
# learner.fit_onecycle(lr=5e-3, epochs=2)

# training using SGDR 2 epoch, 1 epoch for every cycle
# learner.fit(5e-3, 2, cycle_len=1)

# training using SGDR 4 epoch, 2 epoch for evey cycle
# learner.fit(8e-4, 2, cycle_len=2, checkpoint_folder='/Ktrain/checkpoints/SGDR')

# training using SGDR 2 epoch, 1 epoch for every cycle
learner.fit(8e-4, 2, cycle_len=1)

# Validation
learner.validate()
# Plot
learner.plot('lr')
learner.plot('loss')



plt.show(block=True)
plt.interactive(False)
