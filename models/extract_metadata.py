import exifread


def extract_metadata(file_path):
    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f)
            metadata = {}
            for tag in tags.keys():
                if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                    metadata[tag] = str(tags[tag])
            return metadata
    except Exception as e:
        print(f"Error: {e}")
        return None
