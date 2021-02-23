import os
import glob
import argparse

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_path', type=str, help='Full path for dataset, / at EOF')
    parser.add_argument('--ratio_train', type=float, help='Default value = 0.8')
    parser.add_argument('--ratio_test', type=float, help='Default value = 0.15')
    parser.add_argument('--ratio_val', type=float, help='Default value = 0.05')
    parser.print_help()

    return parser.parse_args()

def train_test_split(n_total,p_train=0.8,p_test=0.15,p_val=0.05):
    n_train = int(n_total*p_train)
    n_test = int(n_total*p_test)
    if (n_total*p_val) <= (n_total-n_train-n_test):
        n_val = n_total*p_val
    else:
        n_val = n_total-n_train-n_test

    return n_train, n_test, n_val

def write_label(dataset_path, ratio_train, ratio_test, ratio_val):
    n_train, n_test, n_val = train_test_split(len(os.listdir(dataset_path)), ratio_train, ratio_test, ratio_val)
    train_filename = dataset_path + 'annotation_train.txt'
    val_filename = dataset_path + 'annotation_val.txt'
    test_filename = dataset_path + 'annotation_test.txt'
    dict_filename = dataset_path + 'lexicon.txt'
    txt_files = [train_filename, test_filename, val_filename, dict_filename]

    for txt in txt_files:
        if os.path.exists(txt):
            os.remove(txt)

    for n, img_file in enumerate(glob.glob(os.path.join(dataset_path, '*.jpg')), start=0):
        with open(dict_filename, 'a') as dictfile:
            label = img_file.split('/')[-1].split('_')[1].split('.')[0]
            dictfile.write('{0}\n'.format(label))

        if n <= n_train:
            with open(train_filename, 'a') as trainfile:
                trainfile.write('{0} {1}\n'.format(img_file, n))
        elif (n<=n_test+n_train) and (n>n_train):
            with open(test_filename, 'a') as testfile:
                testfile.write('{0} {1}\n'.format(img_file, n))
        elif n>=(n_test+n_train):
            with open(val_filename, 'a') as valfile:
                valfile.write('{0} {1}\n'.format(img_file, n))
    	

if __name__ == '__main__':
    
    args = init_args()
    if os.path.exists(args.dataset_path):
        write_label(args.dataset_path, args.ratio_train, args.ratio_test, args.ratio_val)
        # write_label1(args.dataset_path)
        print('Write label successful!')
    else:
        print('Dataset directory not exists. Please select valid directory')
    
