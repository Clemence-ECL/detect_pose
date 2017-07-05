import numpy as np
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
# from keras import optimizers
from keras import regularizers
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
# from keras.utils import np_utils


# dimensions of our images.
img_width, img_height = 150, 150

top_model_weights_path = 'bottleneck_fc_model.h5'
train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
nb_train_samples = 3808
nb_validation_samples = 944
epochs = 20
batch_size = 16


def save_bottlebeck_features():
  datagen = ImageDataGenerator(rescale=1. / 255)

  # build the VGG16 network
  model = applications.VGG16(include_top=False, weights='imagenet')

  generator = datagen.flow_from_directory(
      train_data_dir,
      target_size=(img_width, img_height),
      batch_size=batch_size,
      class_mode=None,
      shuffle=False)
  bottleneck_features_train = model.predict_generator(
      generator, nb_train_samples // batch_size)
  np.save('bottleneck_features_train.npy',
          bottleneck_features_train)

  generator = datagen.flow_from_directory(
      validation_data_dir,
      target_size=(img_width, img_height),
      batch_size=batch_size,
      class_mode=None,
      shuffle=False)
  bottleneck_features_validation = model.predict_generator(
      generator, nb_validation_samples // batch_size)
  np.save('bottleneck_features_validation.npy',
          bottleneck_features_validation)

def train_top_model():
  train_data = np.load(open('bottleneck_features_train.npy','rb'))
  train_labels = np.array(
    [0]*(nb_train_samples //2)+[1]*(nb_train_samples//2))
  validation_data = np.load(open('bottleneck_features_validation.npy','rb'))
  validation_labels = np.array(
    [0]*(nb_validation_samples//2)+[1]*(nb_validation_samples//2))


  model = Sequential()
  model.add(Flatten(input_shape=train_data.shape[1:]))
  model.add(Dense(256, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(1, activation='sigmoid'))


  # rmsprop = optimizers.RMSprop(lr = 0.001)
  model.compile(optimizer='rmsprop',
                loss='binary_crossentropy', metrics=['accuracy'])

  model.fit(train_data, train_labels,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=(validation_data, validation_labels))

  model.save_weights(top_model_weights_path)


save_bottlebeck_features()
train_top_model()


# def predict_image_class(file):
#   model = applications.VGG16(include_top=False, weights='imagenet')
#   x = load_img(file, target_size=(img_width,img_ht))
#   x = img_to_array(x)
#   x = np.expand_dims(x, axis=0)
#   array = model.predict(x)
#   model = Sequential()
#   model.add(Flatten(input_shape=array.shape[1:]))
#   model.add(Dense(256, activation='relu'))
#   model.add(Dropout(0.5))
#   model.add(Dense(1, activation='sigmoid'))
#   model.load_weights(top_model_wt_path)
#   class_predicted = model.predict_classes(array)
#   if class_predicted==1:
#     print("dogs")
#   else:
#     print("cat")


# predict_image_class(test_dir + "/cat/cat.3120.jpg")
