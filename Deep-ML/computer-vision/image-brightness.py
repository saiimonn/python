def calculate_brightness(img):
    if not img:
        return -1
    
    rows = len(img)
    cols = len(img[0])

    sum = 0
    count = 0
    for i in range(rows):
        if len(img[i]) != cols:
            return -1
        for j in range(cols):
            if img[i][j] > 255 or img[i][j] < 0:
                return -1
            sum += img[i][j]
            count += 1

    return sum / count

print(calculate_brightness([[100, 200], [50, 150]]))
