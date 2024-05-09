"""
Basic debugging program meant for testing long-term usage and logging failures.
Specifically, to check exceptions from VERIFY function in _k4a.py, _k4abt.py
Continuously captures and processes image and skeleton data. 
Only terminates manually.
"""

import pykinect_azure as pykinect
import logging
import time

def get_current_timestamp():
    try:
        current_time_ns = time.time_ns()
        timestamp_seconds = current_time_ns // 1000000000
        timestamp_nanoseconds = current_time_ns % 1000000000
        return timestamp_seconds, timestamp_nanoseconds
    except Exception as e:
        logging.error(f'Timestamp acquisition failed: {e}')

pykinect.initialize_libraries(track_body=True)
device_config = pykinect.default_configuration
device_config.color_resolution = pykinect.K4A_COLOR_RESOLUTION_720P
device_config.depth_mode = pykinect.K4A_DEPTH_MODE_NFOV_UNBINNED
device_config.color_format = pykinect.K4A_IMAGE_FORMAT_COLOR_MJPG
device_config.camera_fps = pykinect.K4A_FRAMES_PER_SECOND_30
device_config.synchronized_images_only = True

device = pykinect.start_device(config=device_config)
body_tracker = pykinect.start_body_tracker()

logs_path = r'C:\YOUR_REPO\logs\YOURLOG.log'
logging.basicConfig(filename=logs_path,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    logging.debug('Starting data capture')
    while True:
        try:
            sec, nsec = get_current_timestamp()
            logging.debug(f'Timestamp: {sec}, {nsec}')

            logging.debug('Capturing rgb')
            capture = device.update()
            logging.debug('Captured rgb')

            logging.debug('Capturing humans')
            body_frame = body_tracker.update()
            logging.debug('Captured humans')

            logging.debug('Extracting rgb')
            ret, color_image = capture.get_color_image()
            if not ret:
                logging.error('No rgb data returned')
                continue
            else:
                logging.debug(f'rgb: {color_image.shape}')

            logging.debug('Extracting skeletons')
            num_humans = body_frame.get_num_bodies()
            if num_humans == 0:
                logging.info('No humans detected')
            humans = body_frame.get_bodies()

        except KeyboardInterrupt:
            logging.info('User stopped program')
            break
        except Exception as e:
            logging.error(f'Error during processing: {e}')
            continue

finally:
    logging.critical('Application shutting down')
