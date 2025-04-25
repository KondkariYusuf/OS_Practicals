pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frame_size = 3
frames = []
page_faults = 0

for page in pages:
    if page not in frames:
        if len(frames) < frame_size:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)
        page_faults += 1
    print(f"Page: {page} -> Frames: {frames}")

print("\nTotal Page Faults:", page_faults)
