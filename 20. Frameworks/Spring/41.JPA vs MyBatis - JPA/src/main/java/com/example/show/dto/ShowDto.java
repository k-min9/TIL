package com.example.show.dto;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class ShowDto {
  
  private int show_count = 0;
  private int show_charge = 0;
  private int show_time = 0;
  private float charge_reduction  = 0.0f;

}
