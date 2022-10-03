
```

# (.ring 2 )CPU:special-code

: on_init

    # I[ : win1-reg 
    #     I[ : win1-reg-0 'Hello'World . CR ; ]I
    #     (.add_mouse_move_handler {} 'win1-reg-0 }.callback= )dpg 
    # ; ]I
    # (.win1-reg )dpg:handler_registry

    I[ : WIN-1

        (.add_text 'Hello'World )dpg? 'label_tag !
        I[ :? <UNIQUE> (.add_text ("The hover") {} )dpg ; ]I
        (. 'label_tag @ {} )dpg:tooltip

        # ( I[ drop drop ]I )

        # (.add_text 'Hello'World )dpg? 'label_tag !
        # I[ : win1-hover-0 (.add_text ("The hover") {} )dpg ; ]I
        # (.win1-hover-0 'label_tag @ {} )dpg:tooltip

        # (.add_text 'Hello'World'II {} 'foobar2 }.tag= )dpg? 'label_tag !
        # I[ : <UNIQUE> (.add_text ("The hover II") {} )dpg ; ]I
        # (. DUP 'foobar2 {} )dpg:tooltip DROP

        (["One","Two","Three"]) DO 
        (.add_input_int { 'label 'Input V + } )dpg? 'input_tag !
        LOOP

        I[ : press-me
            (.get_value 'input_tag @ )dpg? 'value !
            (.set_value 'label_tag @ 'value @ )dpg
        ; ]I

        (.add_button { 'callback 'press-me 'label 'Press'me } )dpg

        { 'label 'float 'default_value 0.273 'max_value 1 }
        (.add_slider_float dup )dpg drop

        ({"label":"string", "default_value":"Quick brown fox"})
        (.add_input_text dup )dpg drop

    ; ]I

    I[ :? <UNIQUE> 'Window'Closed . CR ; ]I 'tmp-0 !

    'WIN-1 (. {
            'label 'Hello
            'on_close 'tmp-0 @
            'width 500 'height 500
            } )DPG:window



;

on_init

```