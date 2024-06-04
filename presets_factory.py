from features import Features

default_dict = {
    "number_of_outer_rings" : 5,
    "outer_ring_exponential_distance" : 0.99,

    "wave_speed" : 2,
    "wave_frequency" : 0,
    "wave_amplitude" : 50,

    "more_rings_are_larger" : True,


    "feature_to_layer_modifier" : {
        Features.Unordered : 0,
        Features.FaceOval : 0,
        Features.LeftEye : -2,
        Features.RightEye : -2,
        Features.Lips: -2,
        Features.Nose: -2
    },

    "is_feature_included" : {
        Features.FaceOval : True,
        Features.LeftEye : True,
        Features.RightEye : True,
        Features.Lips: True,
        Features.Nose: True
    },

    "list_to_have_extra_waves" : (
        Features.Unordered,
        Features.FaceOval,
        Features.LeftEye,
        Features.RightEye,
        Features.Lips,
        Features.Nose
    ),
        
    
    "wave_potential_colors" : 
        (
            (147, 187, 241),  # deep blue
            (16, 85, 201),
            (55, 121, 234),
            (203, 231, 237),
            (17, 50, 154),
            (231, 69, 77)
        )

    

}



def create_eye_double_helixes():
    dict = {
        "number_of_outer_rings" : 1,
        "outer_ring_exponential_distance" : 0.99,

        "wave_speed" : 2.6,
        "wave_frequency" : 3.4,
        "wave_amplitude" : 13,

        "more_rings_are_larger" : True,


        "feature_to_layer_modifier" : {
            Features.Unordered : 0,
            Features.FaceOval : 0,
            Features.LeftEye : -2,
            Features.RightEye : -2,
            Features.Lips: -2,
            Features.Nose: -2
        },

        "is_feature_included" : {
            Features.FaceOval : None,
            Features.LeftEye : True,
            Features.RightEye : True,
            Features.Lips: None,
            Features.Nose: None
        },
        
        "wave_potential_colors" : 
            (
                (147, 187, 241),  # deep blue
                (16, 85, 201),
                (55, 121, 234),
                (203, 231, 237),
                (17, 50, 154),
                (231, 69, 77)
            )

        

    }
    for key, value in dict.items():
        default_dict[key] = value

    return default_dict


def create_wave_bubbles():
    dict = {
        "number_of_outer_rings" : 3,
        "outer_ring_exponential_distance" : 0.99,

        "wave_speed" : 0.65,
        "wave_frequency" : 0,
        "wave_amplitude" : 100,

        "more_rings_are_larger" : True,


        "feature_to_layer_modifier" : {
            Features.Unordered : -3,
            Features.FaceOval : -3,
            Features.LeftEye : -3,
            Features.RightEye : -3,
            Features.Lips: -3,
            Features.Nose: -3
        },

        "is_feature_included" : {
            Features.FaceOval : True,
            Features.LeftEye : True,
            Features.RightEye : True,
            Features.Lips: True,
            Features.Nose: True
        },

        "list_to_have_extra_waves" : (
            # Features.Unordered,
            Features.FaceOval,
            # Features.LeftEye,
            # Features.RightEye,
            # Features.Lips,
            # Features.Nose
        ),
        
        "wave_potential_colors" : 
            (
                (255, 234, 205),
                (251, 250, 231),
                (253, 255, 250),
                (255, 246, 217),
                (255, 255, 238)
            )

        

    }
    for key, value in dict.items():
        default_dict[key] = value

    return default_dict

def create_face_double_helix():
    dict = {
        "number_of_outer_rings" : 1,
        "outer_ring_exponential_distance" : 0.99,

        "wave_speed" : 2,
        "wave_frequency" : 3.4,
        "wave_amplitude" : 60,

        "more_rings_are_larger" : True,


        "feature_to_layer_modifier" : {
            Features.Unordered : -3,
            Features.FaceOval : 0,
            Features.LeftEye : -3,
            Features.RightEye : -3,
            Features.Lips: -3,
            Features.Nose: -3
        },

        "is_feature_included" : {
            Features.FaceOval : True,
            Features.LeftEye : True,
            Features.RightEye : True,
            Features.Lips: True,
            Features.Nose: True
        },

        "list_to_have_extra_waves" : (
            # Features.Unordered,
            Features.FaceOval,
            # Features.LeftEye,
            # Features.RightEye,
            # Features.Lips,
            # Features.Nose
        ),
        
        # "wave_potential_colors" : 
        #     (
        #         (255, 234, 205),
        #         (251, 250, 231),
        #         (253, 255, 250),
        #         (255, 246, 217),
        #         (255, 255, 238)
        #     )

        

    }
    for key, value in dict.items():
        default_dict[key] = value

    return default_dict

def create_many_face_double_helix():
    dict = {
        "number_of_outer_rings" : 7,
        "outer_ring_exponential_distance" : 1.3,

        "wave_speed" : 2,
        "wave_frequency" : 3.4,
        "wave_amplitude" : 60,

        "more_rings_are_larger" : True,


        "feature_to_layer_modifier" : {
            Features.Unordered : -3,
            Features.FaceOval : 0,
            Features.LeftEye : -3,
            Features.RightEye : -3,
            Features.Lips: -3,
            Features.Nose: -3
        },

        "is_feature_included" : {
            Features.FaceOval : True,
            Features.LeftEye : True,
            Features.RightEye : True,
            Features.Lips: True,
            Features.Nose: True
        },

        "list_to_have_extra_waves" : (
            # Features.Unordered,
            Features.FaceOval,
            # Features.LeftEye,
            # Features.RightEye,
            # Features.Lips,
            # Features.Nose
        ),
        
        # "wave_potential_colors" : 
        #     (
        #         (255, 234, 205),
        #         (251, 250, 231),
        #         (253, 255, 250),
        #         (255, 246, 217),
        #         (255, 255, 238)
        #     )

        

    }
    for key, value in dict.items():
        default_dict[key] = value

    return default_dict


def create_inward_pointing_things():
    dict = {
        "number_of_outer_rings" : 12,
        "outer_ring_exponential_distance" : 0.97,

        "wave_speed" : 6,
        "wave_frequency" : 0.7,
        "wave_amplitude" : 50,

        "more_rings_are_larger" : False,


        "feature_to_layer_modifier" : {
            Features.Unordered : -3,
            Features.FaceOval : -2,
            Features.LeftEye : -3,
            Features.RightEye : -3,
            Features.Lips : -3,
            Features.Nose : 0
        },

        "is_feature_included" : {
            Features.FaceOval : True,
            Features.LeftEye : True,
            Features.RightEye : True,
            Features.Lips: True,
            Features.Nose: True
        },

        "list_to_have_extra_waves" : (
            Features.Unordered,
            Features.FaceOval,
            Features.LeftEye,
            Features.RightEye,
            Features.Lips,
            Features.Nose
        ),
        
        # "wave_potential_colors" : 
        #     (
        #         (255, 234, 205),
        #         (251, 250, 231),
        #         (253, 255, 250),
        #         (255, 246, 217),
        #         (255, 255, 238)
        #     )

        

    }
    for key, value in dict.items():
        default_dict[key] = value

    return default_dict


def create_super_cool_ending():
    # Get rid of over-time wave fade away
    import wave_functionality
    wave_functionality.turn_off_wave_fade_away()
    # Main line 276 layer = int(-i/5)
    dict = {
        "number_of_outer_rings" : 12,
        "outer_ring_exponential_distance" : 0.85,

        "wave_speed" : 1,
        "wave_frequency" : 0.1,
        "wave_amplitude" : 50,

        "more_rings_are_larger" : False,


        "feature_to_layer_modifier" : {
            Features.Unordered : -3,
            Features.FaceOval : -2,
            Features.LeftEye : -3,
            Features.RightEye : -3,
            Features.Lips : -3,
            Features.Nose : 0
        },

        "is_feature_included" : {
            Features.FaceOval : True,
            Features.LeftEye : True,
            Features.RightEye : True,
            Features.Lips: True,
            Features.Nose: True
        },

        "list_to_have_extra_waves" : (
            Features.Unordered,
            Features.FaceOval,
            Features.LeftEye,
            Features.RightEye,
            Features.Lips,
            Features.Nose
        ),
        
        # "wave_potential_colors" : 
        #     (
        #         (255, 234, 205),
        #         (251, 250, 231),
        #         (253, 255, 250),
        #         (255, 246, 217),
        #         (255, 255, 238)
        #     )

        

    }
    for key, value in dict.items():
        default_dict[key] = value

    return default_dict


def nothing():
    # Get rid of over-time wave fade away
    import wave_functionality
    wave_functionality.turn_off_wave_fade_away()
    # Main line 276 layer = int(-i/5)
    dict = {
        "number_of_outer_rings" : 12,
        "outer_ring_exponential_distance" : 0.85,

        "wave_speed" : 1,
        "wave_frequency" : 0.1,
        "wave_amplitude" : 50,

        "more_rings_are_larger" : False,


        "feature_to_layer_modifier" : {
            Features.Unordered : -3,
            Features.FaceOval : -2,
            Features.LeftEye : -3,
            Features.RightEye : -3,
            Features.Lips : -3,
            Features.Nose : 0
        },

        "is_feature_included" : {
            Features.FaceOval : None,
            Features.LeftEye : None,
            Features.RightEye : None,
            Features.Lips: None,
            Features.Nose: None
        },

        "list_to_have_extra_waves" : (
            # Features.Unordered,
            # Features.FaceOval,
            # Features.LeftEye,
            # Features.RightEye,
            # Features.Lips,
            # Features.Nose
        ),
        
        # "wave_potential_colors" : 
        #     (
        #         (255, 234, 205),
        #         (251, 250, 231),
        #         (253, 255, 250),
        #         (255, 246, 217),
        #         (255, 255, 238)
        #     )

        

    }
    for key, value in dict.items():
        default_dict[key] = value

    return default_dict


if __name__ == "__main__":
    import main 
    main.main()