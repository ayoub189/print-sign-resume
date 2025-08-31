def range_spliter(total_pages, pause_points):
    pause_points = sorted(set(pause_points))  
    result = []

    start = 1
    for pause in pause_points:
        pause = int(pause)
        if pause < start:
            continue 
        if pause >= total_pages:
            continue
        if pause == start:
            result.append(f"{start}")
        else:
            result.append(f"{start}-{pause}")
        start = pause + 1

    # Add the last range if any pages are left
    if start <= total_pages:
        if start == total_pages:
            result.append(f"{start}")
        else:
            result.append(f"{start}-{total_pages}")
    return result

