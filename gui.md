
```

# (.ring 2 )CPU:special-code

: win1

    (.add_text 'Hello'World {} 'foobar }.tag= )dpg? 'label_tag !

    I[ : win1-hover (.add_text ("The hover") {} )dpg ; ]I
    (.tooltip 'foobar {} )dpg:win1-hover

    (.add_input_int {} }.label="Input" )dpg? 'input_tag !

    I[ : on-press-0  
    (.get_value 'input_tag @ )dpg? 'value !
    (.set_value 'label_tag @ 'value @ )dpg
    ; ]I

    (["One","Two","Three"]) DO 
    (.add_button {} ("'") V + ''on-press-0 + }.callback=  V }.label= )dpg
    LOOP

    {} }.label="float" }.default_value=0.273 }.max_value=1 'settings !
    (.add_slider_float 'settings @ )dpg

    ({"label":"string", "default_value":"Quick brown fox"})
    (.add_input_text dup )dpg drop




;

: hello 'Hello'World . CR ;

: win1-reg 

    (.add_mouse_move_handler {} }.callback="hello" )dpg
;

: on_init

    (.handler_registry )dpg:win1-reg

    (.window {} 
            }.label="Hello" 
            }.on_close="hello" 
            }.width=500
            }.height=500
            )DPG:win1

;

on_init

```