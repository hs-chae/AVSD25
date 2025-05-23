# from .rules import *
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import numpy as np
# import random

# def plot_triangle(ax, triangle):
#     triangle_patch = patches.Polygon(triangle.points, closed=True, edgecolor=triangle.edgecolor,
#                                      facecolor=triangle.facecolor, alpha=triangle.alpha, label=triangle.label)
#     ax.add_patch(triangle_patch)

# def plot_rectangle(ax, rectangle):
#     rect_patch = patches.Rectangle(rectangle.xy, rectangle.width, rectangle.height,
#                                    edgecolor=rectangle.edgecolor, facecolor=rectangle.facecolor, 
#                                    alpha=rectangle.alpha, label=rectangle.label)
#     ax.add_patch(rect_patch)

# def plot_parallelogram(ax, parallelogram):
#     parallelogram_patch = patches.Polygon(parallelogram.points, closed=True, edgecolor=parallelogram.edgecolor,
#                                            facecolor=parallelogram.facecolor, alpha=parallelogram.alpha, 
#                                            label=parallelogram.label)
#     ax.add_patch(parallelogram_patch)

# def plot_circle(ax, circle):
#     circle_patch = patches.Circle(circle.xy, circle.radius, edgecolor=circle.edgecolor, 
#                                   facecolor=circle.facecolor, alpha=circle.alpha, label=circle.label)
#     ax.add_patch(circle_patch)

# def plot_ellipse(ax, ellipse):
#     ellipse_patch = patches.Ellipse(ellipse.xy, ellipse.width, ellipse.height,
#                                     edgecolor=ellipse.edgecolor, facecolor=ellipse.facecolor, 
#                                     alpha=ellipse.alpha, label=ellipse.label)
#     ax.add_patch(ellipse_patch)

# def plot_regular_polygon(ax, regular_polygon):
#     polygon_patch = patches.RegularPolygon(
#             regular_polygon.xy, regular_polygon.numVertices, radius = regular_polygon.radius,  # 위치, 꼭짓점 수, 반지름
#             edgecolor=regular_polygon.edgecolor,          # 선 색
#             facecolor=regular_polygon.facecolor,          # 채우기 색
#             alpha=regular_polygon.alpha,                  # 투명도
#             label=regular_polygon.label                   # 레이블
#         )
#     ax.add_patch(polygon_patch)

# def plot_function(ax, function):
#     ax.plot(function.x_vals, function.y_vals, color=function.color, label=f'{function.label}(x)')
#     ax.axhline(0, color='black', linewidth=1)
#     ax.axvline(0, color='black', linewidth=1)
#     ax.scatter(function.roots, [0]*len(function.roots), color='red', zorder=5)
#     ax.scatter([0], [function.y_intercept], color='red', zorder=5)

#     tick_interval = random.choice([1, 2])  # 눈금 간격을 랜덤하게 1 또는 2로 설정
#     x_ticks = np.arange(
#         int(function.x_range[0] // tick_interval) * tick_interval, 
#         int(function.x_range[1] // tick_interval + 1) * tick_interval, 
#         tick_interval
#     )
#     ax.set_xticks(x_ticks)

# def plot_cartesian_point(ax, c_point):
#     ax.scatter(c_point.x, c_point.y, c=c_point.color, alpha=c_point.alpha, s=c_point.size)
#     ax.text(c_point.x, c_point.y, c_point.label, fontsize=12, ha='right', va='bottom')

# def plot_polar_point(ax, p_point):
#     ax.scatter(p_point.theta, p_point.r, c=p_point.color, alpha=p_point.alpha, s=p_point.size)
#     ax.text(p_point.theta, p_point.r, p_point.label, fontsize=12, ha='right', va='bottom')

# def plot_1(ax, diagram):
#     count = 0
#     max_absolute_ftn = 0
#     for triangle in diagram.triangles:
#         plot_triangle(ax, triangle)
#     for rectangle in diagram.rectangles:
#         plot_rectangle(ax, rectangle)
#     for parallelogram in diagram.parallelograms:
#         plot_parallelogram(ax, parallelogram)
#     for circle in diagram.circles:
#         plot_circle(ax, circle)
#     for ellipse in diagram.ellipses:
#         plot_ellipse(ax, ellipse)
#     for regularpolygon in diagram.regularpolygons:
#         plot_regular_polygon(ax, regularpolygon)
#     for ftns in diagram.ftns:
#         plot_function(ax, ftns)
#         count += 1
#         if max(max(ftns.y_vals), -1*min(ftns.y_vals)) > max_absolute_ftn:
#             max_absolute_ftn = max(max(ftns.y_vals), -1*min(ftns.y_vals))
#     for c_point in diagram.c_points:
#         plot_cartesian_point(ax, c_point)
#     if count == 0:
#         ax.set_xlim(-20, 20)
#         ax.set_ylim(-20, 20)
#     else:
#         ax.set_xlim(-11, 11)
#         ax.set_ylim(-1*max_absolute_ftn, max_absolute_ftn)

# def plot_2(ax, diagram):
#     # 여기서는 polar point만 그려주고 있음
#     for p_point in diagram.p_points:
#         plot_polar_point(ax, p_point)

# def plot_diagram(ax, diagram):
#     # diagram.plot_type 이 'cartesian'이면 plot_1,
#     # 그 외('polar1' or 'polar2')면 plot_2 호출
#     if diagram.plot_type == "cartesian":
#         plot_1(ax, diagram)
#     else:
#         plot_2(ax, diagram)


from .rules import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

def plot_triangle(ax, tc, triangle, set_visible = True):
    triangle_patch = patches.Polygon(triangle.points, closed=True, edgecolor=triangle.edgecolor,
                                     facecolor=triangle.facecolor, alpha=triangle.alpha, label=triangle.label)
    ax.add_patch(triangle_patch).set_visible(set_visible)

def plot_rectangle(ax, tc, rectangle, set_visible = True):
    rect_patch = patches.Rectangle(rectangle.xy, rectangle.width, rectangle.height,
                                   edgecolor=rectangle.edgecolor, facecolor=rectangle.facecolor, 
                                   alpha=rectangle.alpha, label=rectangle.label)
    ax.add_patch(rect_patch).set_visible(set_visible)

def plot_parallelogram(ax, tc, parallelogram, set_visible = True):
    parallelogram_patch = patches.Polygon(parallelogram.points, closed=True, edgecolor=parallelogram.edgecolor,
                                           facecolor=parallelogram.facecolor, alpha=parallelogram.alpha, 
                                           label=parallelogram.label)
    ax.add_patch(parallelogram_patch).set_visible(set_visible)

def plot_circle(ax, tc, circle, set_visible = True):
    circle_patch = patches.Circle(circle.xy, circle.radius, edgecolor=circle.edgecolor, 
                                  facecolor=circle.facecolor, alpha=circle.alpha, label=circle.label)
    ax.add_patch(circle_patch).set_visible(set_visible)

def plot_ellipse(ax, tc, ellipse, set_visible = True):
    ellipse_patch = patches.Ellipse(ellipse.xy, ellipse.width, ellipse.height,
                                    edgecolor=ellipse.edgecolor, facecolor=ellipse.facecolor, 
                                    alpha=ellipse.alpha, label=ellipse.label)
    ax.add_patch(ellipse_patch).set_visible(set_visible)

def plot_regular_polygon(ax, tc, regular_polygon, set_visible = True):
    polygon_patch = patches.RegularPolygon(
            regular_polygon.xy, regular_polygon.numVertices, radius = regular_polygon.radius,  # 위치, 꼭짓점 수, 반지름
            edgecolor=regular_polygon.edgecolor,          # 선 색
            facecolor=regular_polygon.facecolor,          # 채우기 색
            alpha=regular_polygon.alpha,                  # 투명도
            label=regular_polygon.label                   # 레이블
        )
    ax.add_patch(polygon_patch).set_visible(set_visible)

def plot_function(ax, tc, ftns, set_visible = True):
    lines = ax.plot(ftns.x_vals, ftns.y_vals, color=ftns.color, label=f'{ftns.label}(x)')
    for line in lines:
        line.set_visible(set_visible)

    hline = ax.axhline(0, color='black', linewidth=1)
    vline = ax.axvline(0, color='black', linewidth=1)
    hline.set_visible(set_visible)
    vline.set_visible(set_visible)

    scatter1 = ax.scatter(ftns.roots, [0]*len(ftns.roots), color='red', zorder=5)
    scatter1.set_visible(set_visible)

    scatter2 = ax.scatter([0], [ftns.y_intercept], color='red', zorder=5)
    scatter2.set_visible(set_visible)


    tick_interval = random.choice([1, 2])  # 눈금 간격을 랜덤하게 1 또는 2로 설정
    x_ticks = np.arange(
        int(ftns.x_range[0] // tick_interval) * tick_interval, 
        int(ftns.x_range[1] // tick_interval + 1) * tick_interval, 
        tick_interval
    )
    ax.set_xticks(x_ticks)

def plot_cartesian_point(ax, tc, c_point, set_visible = True):
    ax.scatter(c_point.x, c_point.y, c=c_point.color, alpha=c_point.alpha, s=c_point.size).set_visible(set_visible)
    tc.append(c_point.x, c_point.y, c_point.label)

def plot_polar_point(ax, tc, p_point, set_visible = True):
    ax.scatter(p_point.theta, p_point.r, c=p_point.color, alpha=p_point.alpha, s=p_point.size).set_visible(set_visible)
    tc.append(p_point.theta, p_point.r, p_point.label)

def plot_1(ax, tc, diagram, set_visible = True):
    count = 0
    max_absolute_ftn = 0
    for triangle in diagram.triangles:
        plot_triangle(ax, tc, triangle, set_visible = True)
    for rectangle in diagram.rectangles:
        plot_rectangle(ax, tc, rectangle, set_visible = True)
    for parallelogram in diagram.parallelograms:
        plot_parallelogram(ax, tc, parallelogram, set_visible = True)
    for circle in diagram.circles:
        plot_circle(ax, tc, circle, set_visible = True)
    for ellipse in diagram.ellipses:
        plot_ellipse(ax, tc, ellipse, set_visible = True)
    for regularpolygon in diagram.regularpolygons:
        plot_regular_polygon(ax, tc, regularpolygon, set_visible = True)
    for ftns in diagram.ftns:
        plot_function(ax, tc, ftns, set_visible = True)
        count += 1
        if max(max(ftns.y_vals), -1*min(ftns.y_vals)) > max_absolute_ftn:
            max_absolute_ftn = max(max(ftns.y_vals), -1*min(ftns.y_vals))
    for c_point in diagram.c_points:
        plot_cartesian_point(ax, tc, c_point, set_visible = True)
    if count == 0:
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
    else:
        ax.set_xlim(-11, 11)
        ax.set_ylim(-1*max_absolute_ftn, max_absolute_ftn)

def plot_2(ax, tc, diagram, set_visible = True):
    # 여기서는 polar point만 그려주고 있음
    for p_point in diagram.p_points:
        plot_polar_point(ax, tc, p_point, set_visible = True)

def plot_diagram(ax, tc, diagram, set_visible = True):
    # diagram.plot_type 이 'cartesian'이면 plot_1,
    # 그 외('polar1' or 'polar2')면 plot_2 호출
    if diagram.plot_type == "cartesian":
        plot_1(ax, tc, diagram, set_visible = True)
    else:
        plot_2(ax, tc, diagram, set_visible = True)
