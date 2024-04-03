import cv2
import os
# from natsort import natsorted

def images_to_video(input_folder, output_video_path, fps=30):
    # Get all files in the input folder
    images = [img for img in os.listdir(input_folder) if img.endswith(".jpg") or img.endswith(".png")]
    ## Sort files naturally (human order) -- done below in sorted(images)
    #images = natsorted(images)

    # Determine the width and height from the first image
    frame = cv2.imread(os.path.join(input_folder, images[0]))
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use lower case
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for image in sorted(images):
        img_path = os.path.join(input_folder, image)
        img = cv2.imread(img_path)
        out.write(img)  # Write out frame to video

    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved as {output_video_path}")

if __name__ == "__main__":
    # Set your input folder and output video path
    input_folder = './output'
    output_video_path = 'output/output_video.mp4'
    fps = 24  # Frames per second

    images_to_video(input_folder, output_video_path, fps)
