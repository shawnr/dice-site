"""
Quick cleanup script to give all ID's unique names.
"""
def clean_file():
    svg_doc = open('app/su_panorama.svg', 'r+')
    clean_svg_doc = open('app/su_panorama_cleaned.svg', 'w+')
    shape_counter = 0
    rect_counter = 0
    group_counter = 0

    for line in svg_doc.readlines():
        if 'id="Shape"' in line:
            shape_counter += 1
            clean_svg_doc.write(
                line.replace('id="Shape"', 'id="Shape%s"' % shape_counter))
        elif 'id="Rectangle"' in line:
            rect_counter += 1
            clean_svg_doc.write(
                line.replace('id="Rectangle"', 'id="Rectangle%s"' % rect_counter))
        elif 'id="Group"' in line:
            group_counter += 1
            clean_svg_doc.write(
                line.replace('id="Group"', 'id="Group%s"' % group_counter))
        else:
            clean_svg_doc.write(line)

    print "FINISHED! Replaced %s Shapes, %s Rects, and %s Groups." % (
        shape_counter, rect_counter, group_counter)
