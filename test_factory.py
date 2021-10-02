from factory import DirectoryListing


def test_pool():
    path = '.'
    dl1 = DirectoryListing.create_directory_listing(path)
    dl2 = DirectoryListing.create_directory_listing(path)

    assert(dl1 == dl2 and 'DirectoryListing objects are not the same')