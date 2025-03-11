import random
import shutil
from pathlib import Path


def split_dataset(verbose=False):
    train_val_ratio = 0.8

    dataset_root = Path("./FlowerDataset")
    categories = dataset_root.glob("Fleurs*")

    train_root = Path("./Flowers/Train")
    if train_root.exists():
        shutil.rmtree(train_root)
    train_root.mkdir(parents=True)

    val_root = Path("./Flowers/Val")
    if val_root.exists():
        shutil.rmtree(val_root)
    val_root.mkdir(parents=True)

    for category in categories:
        nb_data = len(list(category.glob("*.jpg")))

        nb_train = int(nb_data * train_val_ratio)
        nb_val = nb_data - nb_train

        train_category = train_root / category.name
        if not train_category.exists():
            train_category.mkdir(parents=True)

        val_category = val_root / category.name
        if not val_category.exists():
            val_category.mkdir(parents=True)

        data = list(category.glob("*.jpg"))
        random.shuffle(data)

        for i, d in enumerate(data):
            if i < nb_train:
                shutil.copy(d, train_category / d.name)
            else:
                shutil.copy(d, val_category / d.name)

    for category in dataset_root.glob("Fleurs*"):
        nb_train = len(list((train_root / category.name).glob("*.jpg")))
        nb_val = len(list((val_root / category.name).glob("*.jpg")))
        if verbose:
            print(
                f"{category.name}: {nb_train} training images, {nb_val} validation images"
            )


def main():
    split_dataset(verbose=True)


if __name__ == "__main__":
    main()
