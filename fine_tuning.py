from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras.models import Model

# path to the model wieghts files
weights_path = '../keras/examples/vgg16_weights.h5'
top_model_weights_path = 'bottleneck_fc_model.h5'
#dimensions of our images
img_width, img_height = 150, 150

train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
nb_train_samples = 1792
nb_validation_samples = 416
epochs = 15
batch_size = 16

#build the VGG16 network
model = applications.VGG16(weights='imagenet', include_top=False, input_shape=(150,150,3))
print('Model loaded')



#build a classifier moedel to put on top of the convolutional model
top_model = Sequential()
top_model.add(Flatten(input_shape=model.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(1, activation='sigmoid'))

top_model.load_weights(top_model_weights_path)
# model.add(top_model)
model = Model(inputs= model.input, outputs= top_model(model.output))


for layer in model.layers[:15:
  layer.trainable = False

model.compile(loss='binary_crossentropy',
  optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
  metrics=['accuracy'])

train_datagen = ImageDataGenerator(
  rescale=1. /2255,
  shear_range = 0.2,
  zoom_range = 0.2,
  horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale=1. /255)

train_generator = train_datagen.flow_from_directory(
  train_data_dir,
  target_size=(img_height, img_width),
  batch_size=batch_size,
  class_mode='binary')

validation_generator = train_datagen.flow_from_directory(
  validation_data_dir,
  target_size=(img_height, img_width),
  batch_size=batch_size,
  class_mode='binary')

model.fit_generator(
  train_generator,
  samples_per_epoch = nb_train_samples // batch_size,
  epochs = epochs,
  validation_data = validation_generator,
  nb_val_samples = nb_validation_samples // batch_size)

