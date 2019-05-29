import helper
import h5py

def run():
    image_db = helper.read_db()
    helper.extract_ds(image_db)


if __name__ == '__main__':
    run()