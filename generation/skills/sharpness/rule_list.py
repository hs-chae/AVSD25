import inspect




length_rules = ['add_free_point','add_circle','add_free_circle',"circle_with_radius", 'add_free_point_with_line', 'add_line', 
                # 'C_add_free_point', 'C_add_circle', 'C_add_free_circle', 'C_circle_with_radius', 'C_add_free_point_with_line', 'C_add_line',
                    #   'C_length_1', 'C_length_2', 'C_length_3', 'C_length_4', 'C_length_5', 'C_length_6', 'C_length_7', 'C_length_8', 'C_length_9',
                      'length_1','length_2','length_3','length_4','length_5','length_6','length_7','length_8', 'length_9']



color_angle_rules = ['add_free_point','add_circle','add_free_circle',"circle_with_radius",'C_add_free_point', 'C_add_circle', 'C_add_free_circle', 'C_circle_with_radius', 'add_free_point_with_line', 'C_add_free_point_with_line', 'add_line', 'C_add_line',
                    'C_angle1', 'C_angle2', 'C_angle3', 'C_angle4', 'C_angle5', 'C_angle6', 'C_angle7', 'C_angle8', 'C_angle9', 'C_angle10', 'C_angle11', 'C_angle12', 'C_angle13', 'C_angle14', 'C_angle15', 'C_angle16', 'C_angle17',
                    'angle1', 'angle2', 'angle3', 'angle4', 'angle5', 'angle6', 'angle7', 'angle8', 'angle9', 'angle10', 'angle11', 'angle12', 'angle13', 'angle14', 'angle15', 'angle16', 'angle17']

angle_only_rules = [ 'C_angle1', 'C_angle2', 'C_angle3', 'C_angle4', 'C_angle5', 'C_angle6', 'C_angle7', 'C_angle8', 'C_angle9', 'C_angle10', 'C_angle11', 'C_angle12', 'C_angle13', 'C_angle14', 'C_angle15', 'C_angle16', 'C_angle17',
                    'angle1', 'angle2', 'angle3', 'angle4', 'angle5', 'angle6', 'angle7', 'angle8', 'angle9', 'angle10', 'angle11', 'angle12', 'angle13', 'angle14', 'angle15', 'angle16', 'angle17']

color_parallel_rules = [#'add_free_point','add_circle','add_free_circle',"circle_with_radius",'C_add_free_point', 'C_add_circle', 'C_add_free_circle', 'C_circle_with_radius', 'add_free_point_with_line', 'C_add_free_point_with_line', 'add_line', 'C_add_line',
                        'C_parallel_1', 'C_parallel_2', 'C_parallel_3', 'C_parallel_4',
                        'parallel_1','parallel_2','parallel_3','parallel_4', 'parallel_5']


color_length_rules = ['add_free_point','add_circle','add_free_circle',"circle_with_radius",'C_add_free_point', 'C_add_circle', 'C_add_free_circle', 'C_circle_with_radius', 'add_free_point_with_line', 'C_add_free_point_with_line', 'add_line', 'C_add_line',
                      'C_length_1', 'C_length_2', 'C_length_3', 'C_length_4', 'C_length_5', 'C_length_6', 'C_length_7', 'C_length_8', 'C_length_9', 'C_length_12', 'C_length_13', 'C_length_14_1', 'C_length_14_2', 'C_length_15', 'C_length_16', 'C_length_17_1', 'C_length_17_2', 'C_length_17_3', 'C_length_18',
                      'length_1','length_2','length_3','length_4','length_5','length_6','length_7','length_8', 'length_9', 'length_10', 'length_11', 'length_12', 'length_13', 'length_14_1', 'length_14_2', 'length_15', 'length_16', 'length_17_1', 'length_17_2', 'length_17_3',
                      'length_20', 'length_21'
                      ]

length_only_rules = [ 'C_length_1', 'C_length_2', 'C_length_3', 'C_length_4', 'C_length_5', 'C_length_6', 'C_length_7', 'C_length_8', 'C_length_9', 'C_length_12', 'C_length_13', 'C_length_14_1', 'C_length_14_2', 'C_length_15', 'C_length_16', 'length_17_1', 'length_17_2', 'length_17_3',
                      'length_1','length_2','length_3','length_4','length_5','length_6','length_7','length_8', 'length_9', 'length_10', 'length_11', 'length_12', 'length_13', 'length_14_1', 'length_14_2', 'length_15', 'length_16', 'length_17_1', 'length_17_2', 'length_17_3', 'length_18',
                      'C_length_18','length_20', 'length_21']


sharp_rules = [
                        'add_free_point','add_circle','add_free_circle',"circle_with_radius",'C_add_free_point', 'C_add_circle', 'C_add_free_circle', 'C_circle_with_radius', 'add_free_point_with_line', 'C_add_free_point_with_line', 'add_line', 'C_add_line',
                        'sharp1', 'sharp2', 'sharp3', 'sharp1', 'sharp2', 'sharp3', 'sharp1', 'sharp2', 'sharp3', 'sharp1', 'sharp2', 'sharp3'
                        # 'sharp4'
                        ]