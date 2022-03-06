mergeInto(LibraryManager.library, {

  GetSpeed: function (speed) {
    window.dispatchReactUnityEvent("GetSpeed", speed);
  }

});