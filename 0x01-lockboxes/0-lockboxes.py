#!/usr/bin python3

def canUnlockAll(boxes: List) -> bool:
    """
    accepts list of boxes(lists) containing
    keys to other boxes. 
    The first box is always opened.
    
    Return True if all boxes can be opened else False
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
