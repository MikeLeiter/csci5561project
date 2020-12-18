#import os
#os.environ["DLClight"]="True"

import deeplabcut

video_path = '/Users/mikeleiter/Documents/Project/Videos/lion_defenced_seg.avi'
directory = '/Users/mikeleiter/Documents/Project/'

#deeplabcut.create_new_project('lion_final', 'Leiter', [video_path], working_directory = directory, copy_videos = False)

config_path = '/Users/mikeleiter/Documents/Project/lion_final-Leiter-2020-12-08/config.yaml'

#deeplabcut.extract_frames(config_path, mode='automatic')

#deeplabcut.label_frames(config_path)

#deeplabcut.check_labels(config_path)

# deeplabcut.create_training_dataset(config_path, augmenter_type='imgaug')

#deeplabcut.train_network(config_path, shuffle=1, displayiters=10,saveiters=100)

videofile_path = ['/Users/mikeleiter/Documents/Project/Videos/lion_defenced_seg.avi'] #Enter the list of videos to analyze.
#deeplabcut.analyze_videos(config_path, videofile_path, videotype='.avi')

deeplabcut.create_labeled_video(config_path, videofile_path, draw_skeleton=True)








#create a path variable that links to the config file:
#path_config_file = 'examples/openfield-Pranav-2018-10-30/config.yaml'

# Loading example data set:
#deeplabcut.load_demo_data(path_config_file)

#let's also change the display and save_iters just in case Colab takes away the GPU... 
#if that happens, you can reload from a saved point. Typically, you want to train to 200,000 + iterations.
#more info and there are more things you can set: https://github.com/AlexEMG/DeepLabCut/blob/master/docs/functionDetails.md#g-train-the-network

#deeplabcut.train_network(path_config_file, shuffle=1, displayiters=10,saveiters=100)

#this will run until you stop it (CTRL+C), or hit "STOP" icon, or when it hits the end (default, 1.03M iterations). 
#Whichever you chose, you will see what looks like an error message, but it's not an error - don't worry....