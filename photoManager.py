# takePhoto() -> photo filename - Takes a photo and returns its filename

def takePhoto():
    from picamera import PiCamera
    cam = PiCamera()
    cam.resolution = (4056, 3040)
    
    """
    Goal naming convention:
    
    For each image, use the base `image-n.jpg`, where n is an integer value.
    
    Every filename must be unique.
    
    To do this, we can simply use a filename listing and extract, using regex, the numbers:
    
    image-(\d+)\.jpg
    
    Using this, we can generate a match listing with all numbers. To find the highest, we simply do max(numbers)
    """
    
    filename = "image1.jpg" # TODO: Replace with a dynamic filename system
    cam.capture(filename)
    return filename 
