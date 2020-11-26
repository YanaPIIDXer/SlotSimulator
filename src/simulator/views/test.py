from django.http import HttpResponse
import matplotlib.pyplot as plt
import io

def plt_to_svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

def versus_test(request):
    x = [0, 1000, 2000, 3000, 4000]
    y = []
    z = 1.2
    for i in x:
        y.append(i * 10 * z)
        z = z + 1.5
    plt.plot(x, y, label="x")
    plt.xlabel("x")
    plt.ylabel("y")
    svg = plt_to_svg()
    return HttpResponse(svg, content_type='image/svg+xml')
