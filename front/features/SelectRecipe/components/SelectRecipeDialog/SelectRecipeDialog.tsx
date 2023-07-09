"use client";
import * as React from "react";
import Box from "@mui/material/Box";
import { DataGrid, GridColDef } from "@mui/x-data-grid";
import { useSelectRecipeDialog } from "../../hooks/useSelectRecipeDialog";

const SelectRecipeDialog = () => {
  const { recipe } = useSelectRecipeDialog();
  console.log(123);
  const columns: GridColDef[] = [
    { field: "name", headerName: "レシピ名", width: 600 },
    { field: "recipe_materials", headerName: "材料", width: 600 },
    { field: "recipe_indication", headerName: "調理時間", width: 100 },
  ];

  return (
    <Box sx={{ height: "100%" }}>
      <DataGrid
        rows={recipe}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 50,
            },
          },
        }}
        pageSizeOptions={[50]}
        checkboxSelection
        disableRowSelectionOnClick
      />
    </Box>
  );
};

export default SelectRecipeDialog;
