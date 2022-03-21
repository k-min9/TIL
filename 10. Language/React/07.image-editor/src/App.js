import React, { useRef } from "react";
import "tui-image-editor/dist/tui-image-editor.css";
import ImageEditor from "@toast-ui/react-image-editor";

function App() {
  const myTheme = {
    // Theme object to extends default dark theme.
  };
  const imageSERVER = "https://cdn.filestackcontent.com/AM9o5lgXYR1uvQX2NaAqnz/output=secure:true/"
  const editorRef = useRef(null);
    
  const editorFlipX = () => {
    // const editorInstance = editorRef.current.getInstance();
    // editorInstance.flipX();
    editorRef.current.getInstance().flipX();
  }
  const editorAddIcon = () => {editorRef.current.getInstance().addIcon('arrow', {fill:'red'});}
  const editorAddImage = () => {editorRef.current.getInstance().addImageObject(imageSERVER + 'https://docs.unity3d.com/uploads/Main/ShadowIntro.png');}


  return (
    <div>
      <ImageEditor
        ref={editorRef}
        includeUI={{
          loadImage: {
            // 기본사진
            path: "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/be0a9a4b-1957-4a83-a542-fb720a0a660e/d17qhno-e7454092-80aa-4b3d-898a-96198b4a756c.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2JlMGE5YTRiLTE5NTctNGE4My1hNTQyLWZiNzIwYTBhNjYwZVwvZDE3cWhuby1lNzQ1NDA5Mi04MGFhLTRiM2QtODk4YS05NjE5OGI0YTc1NmMuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Kntd9m3HPNC-JF5QcIS3Iew_dNN68BOt4oeiOTj_Rgs",
            // path: "https://docs.unity3d.com/uploads/Main/ShadowIntro.png",
            name: "SampleImage",
          },
          theme: myTheme,
          menu: [
            // 넣고싶은 기능을 이 배열에서 없애거나 추가할 수 있습니다.
            // "resize",
            // "crop",
            "flip",
            "rotate",
            "draw",
            "shape",
            "icon",
            "text",
            "mask",
            "filter",
          ],
          initMenu: "mask",
          uiSize: {
            width: "1000px",
            height: "700px",
          },
          menuBarPosition: "top",
        }}
        cssMaxHeight={500}
        cssMaxWidth={700}
        selectionStyle={{
          cornerSize: 20,
          rotatingPointOffset: 70,
        }}
        usageStatistics={true}
      />
      <button onClick={editorFlipX}> X 좌우 반전 </button>
      <button onClick={editorAddIcon}> 붉은 화살표 </button>
      <button onClick={editorAddImage}> 이미지 추가 </button>
    </div>

  );
}

export default App;
