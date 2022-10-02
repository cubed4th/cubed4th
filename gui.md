
```

: special_code 

'Expecting'2: . CR
PRIV . CR 
CR

;

: on-press:btn2 . CR ( Prints 55 ) 

CR
'Expecting'1: . CR
PRIV . CR 
CR

(.ring 2 {} )ACL:special_code

;

: win1

    'Hello'World 'message !

    (.add_text 'message @ {} )dpg

    (["One","Two","Three"]) DO V . CR 

    (.add_button 
       {}
        }.callback="55'on-press:btn2"
        V }.label=
        )dpg?

        'button'id'=' . . cr

    LOOP

    {} }.label="float" }.default_value=0.273 }.max_value=1 'settings !
    (.add_slider_float 'settings @ )dpg

    ({"label":"string", "default_value":"Quick brown fox"})
    (.add_input_text dup )dpg drop
;

: hello 'Hello'World . CR ;

(.window {} 
          }.label="Hello" 
          }.on_close="hello" 
          )dpg:win1

```